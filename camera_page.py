import os
import sys
import time
import cv2
import tkinter as tk
from tkinter import ttk, filedialog
from tkinter import *
from PIL import Image, ImageTk, ImageGrab
from win32gui import FindWindow, GetWindowRect
import pygetwindow as gw
import numpy as np


from color_detection_file.supporting_file import *
access_cam = True
class App(tk.Frame):
    def __init__(self, parent, show_page_callback):
        super().__init__(parent)
        self.show_page_callback = show_page_callback
        self.access_cam = access_cam
        # Canvas
        self.canvas = Canvas(self, width = 720, height=540, bg="white")
        self.canvas.create_rectangle(0, 0, 720, 75, outline = "light grey", fill="light grey")
        self.canvas.pack()
        self.save_frame = ""
        
        # Color label
        self.colorImage = self.canvas.create_rectangle(140, 16, 190, 66, fill='blue')
        
        self.colorLabel = self.canvas.create_text(200, 32, text='Blue', font= 'Aerial 12', anchor='w')
        
        self.colorHex = self.canvas.create_text(200, 49, text='#FFFFF', font= 'Aerial 12', anchor='w')
        
        # Select detection mode
        self.yMode = 16
        
        # Camera Section
        self.cameraTop = 110
        self.canvas.create_rectangle(115, self.cameraTop, 608, 470, outline = "light grey", fill="light grey")
        
        self.videoLabel = tk.Label(self)
        self.videoLabel.place(x=145, y=self.cameraTop)
        self.webcam = cv2.VideoCapture(0)
                
        # Camera Footer
        # width, height = 433, 325
        # camera bottom y = 415
        select = self.canvas.create_text(528,self.yMode+7,text='Mode:', font='Aerial 14 bold', tags='select-button')
        back = self.canvas.create_text(190, self.cameraTop + 343, text='Back', font='Aerial 12', tags='back-button')
        screenshot = self.canvas.create_text(335, self.cameraTop + 343, text='Screenshot', font='Aerial 12')
        toggle = self.canvas.create_text(510, self.cameraTop + 343, text='Toggle Camera', font='Aerial 12', tags= 'toggle-camera')
        
        # Add underline to buttons
        bboxBack = self.canvas.bbox(back)
        bboxScreenshot = self.canvas.bbox(screenshot)
        bboxToggle = self.canvas.bbox(toggle)
        bboxMode = self.canvas.bbox(select)
        
        self.canvas.create_rectangle(bboxBack[0], bboxBack[3], bboxBack[2], bboxBack[3] + 1, outline='red', fill = 'red')
        self.canvas.create_rectangle(bboxScreenshot[0], bboxScreenshot[3], bboxScreenshot[2], bboxScreenshot[3] + 1, outline='green', fill = 'green')
        self.canvas.create_rectangle(bboxToggle[0], bboxToggle[3], bboxToggle[2], bboxToggle[3] + 1, outline='blue', fill = 'blue')
        self.canvas.create_rectangle( bboxMode[0], bboxMode[3], bboxMode[2], bboxMode[3] + 1, outline='black', fill = 'white')
        # select mode
        self.canvas.tag_bind('select-button','<Button-1>',self.change_mode)
        # Go back to help page
        self.canvas.tag_bind('back-button', '<Button-1>', self.backButton)
        
        # Toggle camera on/off
        self.cameraRunning = True
        self.canvas.tag_bind('toggle-camera', '<Button-1>', self.toggleCamera)
        
        # Page footer
        self.canvas.create_rectangle(0, 540, 720, 500, fill="#D9D9D9", outline = "#D9D9D9")
        self.canvas.create_text(360,520, text="Created by SPARTANS MS-11", fill = "black", font='Aerial 10', tags="text_tag")
        
        self.main()
            
    def main(self):
        print("Main is running")
        self.updateFrame()
    
    def updateFrame(self):
        if self.cameraRunning:
            _, frame = self.webcam.read()
            self.save_frame = frame
            if not self.access_cam:  
                #Showing cam mode
                tk.Label(self,text="Single Color").place(x=600, y= self.yMode)
                tk.Label(self,text="Detection").place(x=600, y= self.yMode + 27) 
                tk_width, tk_height = self.get_tk_win_size()
                aspect_ratio_w = 4
                aspect_ratio_h = 3
                
                pengali = (tk_height / 3) if (tk_width > tk_height) else int(tk_width) / 4
                
                if frame is not None:
                    height, width, _ = frame.shape
                    # change BGR to HSV color format
                    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
                    frame = cv2.flip(frame, 1) # flip frames
                    
                    # get center coordinate (x, y) of window
                    cx = int(width / 2)
                    cy = int(height / 2)
                    
                    # pick pixel value
                    pixel_center = hsv_frame[cy, cx]
                    
                    color = (color_decider(pixel_center))
                    pixel_center_bgr = frame[cy, cx]
                    b, g, r = int(pixel_center_bgr[0]), int(pixel_center_bgr[1]), int(pixel_center_bgr[2])

                    # color = (color_decider(pixel_center))
                    
                    # #testing

                    # hex_value = self.rgb_to_hex(r,g,b)

                    # if color == "undefined":
                    #     self.color = ""
                    # else :
                    #     self.color = color

                    # self.colorframe =tk.Frame( width=70,height=40,bg=hex_value).pack()

                    # self.namacolor = tk.Frame(width =70 ,height=40).pack()
                    # tk.Label(self.namacolor , text=self.color,font=(50)).pack()

                    # add square
                    cv2.rectangle(frame, (cx-5, cy-5), (cx+5, cy+5), (255, 0, 0), 1)

                    # add text
                    cv2.putText(frame, color, (10, 50), 0, 1, (b, g, r), 2)
                    # colorLabel.config(text=color)
                    
                    frame = cv2.resize(frame, (433, 325))
                    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert from BGR to RGB
                    image = Image.fromarray(frame)  # Create an Image object from the frame
                    photo = ImageTk.PhotoImage(image=image)  # Create a PhotoImage from the Image object
                    self.videoLabel.config(image=photo)  # Update the videoLabel with the new image
                    self.videoLabel.image = photo  # Keep a reference to the PhotoImage to prevent garbage collection
                    
                    # Edit GUI color label
                    hex = self.rgb_to_hex(r, g, b)
                    self.canvas.itemconfig(self.colorImage, fill = hex)
                    self.canvas.itemconfig(self.colorLabel, text=color)
                    self.canvas.itemconfig(self.colorHex, text = hex)

                    self.after(10, self.updateFrame)
            else:
                # showing cam mode
                tk.Label(self,text="Multi Color").place(x=600, y= self.yMode)
                tk.Label(self,text="Detection").place(x=600, y= self.yMode + 27) 
                # Reading the video from the
                # webcam in image frames
                # Convert the imageFrame in
                # BGR(RGB color space) to
                # HSV(hue-saturation-value)
                # color space
                hsvFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

                # define mask for each color using range of color
                # mask = cv2.inRange(frame, lower range, upper range)
                black_mask = cv2.inRange(hsvFrame, np.array(color_dict_HSV["black"][1], np.uint8), np.array(color_dict_HSV["black"][0], np.uint8))
                white_mask = cv2.inRange(hsvFrame, np.array(color_dict_HSV["white"][1], np.uint8), np.array(color_dict_HSV["white"][0], np.uint8))
                red_mask = cv2.inRange(hsvFrame, np.array(color_dict_HSV["red"][1], np.uint8), np.array(color_dict_HSV["red"][0], np.uint8))
                Red_mask = cv2.inRange(hsvFrame, np.array(color_dict_HSV["Red"][1], np.uint8), np.array(color_dict_HSV["Red"][0], np.uint8))
                green_mask = cv2.inRange(hsvFrame, np.array(color_dict_HSV["green"][1], np.uint8), np.array(color_dict_HSV["green"][0], np.uint8))
                blue_mask = cv2.inRange(hsvFrame, np.array(color_dict_HSV["blue"][1], np.uint8), np.array(color_dict_HSV["blue"][0], np.uint8))
                yellow_mask = cv2.inRange(hsvFrame, np.array(color_dict_HSV["yellow"][1], np.uint8), np.array(color_dict_HSV["yellow"][0], np.uint8))
                purple_mask = cv2.inRange(hsvFrame, np.array(color_dict_HSV["purple"][1], np.uint8), np.array(color_dict_HSV["purple"][0], np.uint8))
                orange_mask = cv2.inRange(hsvFrame, np.array(color_dict_HSV["orange"][1], np.uint8), np.array(color_dict_HSV["orange"][0], np.uint8))
                brown_mask = cv2.inRange(hsvFrame, np.array(color_dict_HSV["brown"][1], np.uint8), np.array(color_dict_HSV["brown"][0], np.uint8))
                


                # Morphological Transform, Dilation
                # for each color and bitwise_and operator
                # between imageFrame and mask determines
                # to detect only that particular color
                kernel = np.ones((5, 5), "uint8")

                # For red color
                black_mask = cv2.dilate(black_mask, kernel)
                res_black = cv2.bitwise_and(frame, frame,
                                        mask = black_mask)
                # For red color
                white_mask = cv2.dilate(white_mask, kernel)
                res_white = cv2.bitwise_and(frame, frame,
                                        mask = white_mask)
                # For red color
                red_mask = cv2.dilate(red_mask, kernel)
                res_red = cv2.bitwise_and(frame, frame,
                                        mask = red_mask)
                # For red color
                Red_mask = cv2.dilate(Red_mask, kernel)
                res_Red = cv2.bitwise_and(frame, frame,
                                        mask = Red_mask)
                # For green color
                green_mask = cv2.dilate(green_mask, kernel)
                res_green = cv2.bitwise_and(frame, frame,
                                            mask = green_mask)
                # For blue color
                blue_mask = cv2.dilate(blue_mask, kernel)
                res_blue = cv2.bitwise_and(frame, frame,
                                        mask = blue_mask)
                    # For blue color
                yellow_mask = cv2.dilate(yellow_mask, kernel)
                res_yellow = cv2.bitwise_and(frame, frame,
                                        mask = yellow_mask)
                # For blue color
                purple_mask = cv2.dilate(purple_mask, kernel)
                res_purple = cv2.bitwise_and(frame, frame,
                                        mask = purple_mask)
                # For blue color
                orange_mask = cv2.dilate(orange_mask, kernel)
                res_orange = cv2.bitwise_and(frame, frame,
                                        mask = orange_mask)
                # For blue color
                brown_mask = cv2.dilate(brown_mask, kernel)
                res_brown = cv2.bitwise_and(frame, frame,
                                        mask = brown_mask)
                
                color_mask_list = [black_mask,white_mask,red_mask,Red_mask,green_mask,blue_mask,yellow_mask,
                        purple_mask,orange_mask,brown_mask]
                for order in range(0,10):
                    # Creating contour to track each color
                    contours, hierarchy = cv2.findContours(color_mask_list[order],
                                                        cv2.RETR_TREE,
                                                        cv2.CHAIN_APPROX_SIMPLE)

                    for pic, contour in enumerate(contours):
                        area = cv2.contourArea(contour)
                        if(area > 1500): #Size of color detected
                            x, y, w, h = cv2.boundingRect(contour)
                            frame = cv2.rectangle(frame, (x, y),
                                                    (x + w, y + h),
                                                    tuple(color_dict_BGR[color_list[order]]), 2)
                            
                            cv2.putText(frame, color_list[order], (x, y),
                                        cv2.FONT_HERSHEY_SIMPLEX, 1.0,
                                        tuple(color_dict_BGR[color_list[order]]))	
                frame = cv2.resize(frame, (433, 325))
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert from BGR to RGB
                image = Image.fromarray(frame)  # Create an Image object from the frame
                photo = ImageTk.PhotoImage(image=image)  # Create a PhotoImage from the Image object
                self.videoLabel.config(image=photo)  # Update the videoLabel with the new image
                self.videoLabel.image = photo  #	
                        
                self.after(10, self.updateFrame) # Rerun updateFrame function after 10 miliseconds

    def backButton(self, event):
        self.show_page_callback('page2')
        
    def screenshot(self):
        x, y, w, h = self.winfo_x(), self.winfo_y(), self.winfo_width(), self.winfo_height()
        
        print(x, y, x+w, y+h)
        
        screenshot = ImageGrab.grab(bbox=(x, y, x + w + 200, y + h + 200))
        path = filedialog.asksaveasfilename(defaultextension='.png', filetypes=[("PNG files", "*.png"), ("All Files", "*.*")])
        
        if path:
            screenshot.save(path)
        
    def toggleCamera(self, event):
        self.cameraRunning = not self.cameraRunning
        if self.cameraRunning:
            self.startCamera()
        else:
            self.stopCamera()
    
    def startCamera(self):
        self.cameraRunning = True
        self.videoLabel.destroy()
        
        self.videoLabel = tk.Label(self, text = 'Starting up camera')
        self.videoLabel.place(x=265, y = 275)
        
        self.videoLabel.destroy()
        self.videoLabel = tk.Label(self)
        self.videoLabel.place(x=145, y=self.cameraTop)
        self.webcam = cv2.VideoCapture(0)
        
        self.updateFrame()
        
    def stopCamera(self):
        self.cameraRunning = False
        self.webcam.release()
        
        self.videoLabel.destroy()
        self.videoLabel = tk.Label(self, text="Video camera has been turned off.")
        self.videoLabel.place(x=265, y = 255)
    
    def get_tk_win_size(self):
        return self.winfo_width(), self.winfo_height()
    
    def rgb_to_hex(self, r, g, b):
        return '#{:02x}{:02x}{:02x}'.format(r, g, b)
    def change_mode(self,event):
        self.access_cam = not self.access_cam
