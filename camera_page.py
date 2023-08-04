import os
import sys
import cv2
import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageTk, ImageGrab

from win32gui import FindWindow, GetWindowRect
import pygetwindow as gw


from color_detection_file.supporting_file import *

def rgb_to_hex(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

class App(tk.Frame):
    
    def __init__(self, parent):
        super().__init__(parent)
        
        # self.minsize(1100,540)
        # self.geometry("720x540")
        self.save_frame = ""
        # self.title('color')
        
        # Column 2 - Camera
        self.videoLabel = tk.Label(self)
        self.videoLabel.grid(row=1, column=1, columnspan=3,sticky="W")
        self.webcam = cv2.VideoCapture(0)
                
        # Column 3 - Back Button
        self.back = ttk.Button(self, text="Back")
        self.back# .grid(row=2,column=0)
        
        #warna
        
        
        #mode
        self.mode= tk.Frame(width=140,height=50) #.grid(row = 0,column= 3,padx=50,pady=10)
        tk.Label(self.mode,text="Single Color " ) #.grid(row = 0,column= 3,padx=5,pady=10,sticky="NW")
        tk.Label(self.mode,text="Detection" ) #.grid(row = 0,column= 3,padx=5,pady=10,sticky="SW")
        #switch mode 
        self.switch = ttk.Button(self, text ="switch mode").grid(row=0,column=3)
        
        # photo button

        self.photo = ttk.Button(self, text="Take Photo", command = self.screenshot)
        self.photo.grid(row=2, column=1)
        
        # Column 3 - Toggle Camera Button
        self.toggle = tk.BooleanVar()
        self.toggle.set(True)
        self.cameraRunning = True
        self.toggleCamera = tk.Checkbutton(self, text="Toggle Camera", variable = self.toggle, command=self.toggleCamera)
        self.toggleCamera.grid(row=2, column=2)
        
        # proportional size
        for i in range(3):
            self.rowconfigure(i, weight = 1)
            self.columnconfigure(i, weight = 1)
            
        self.after(1000, self.main)
            
    def main(self):
        self.updateFrame()
        
    def screenshot(self):
        x, y, w, h = self.winfo_x(), self.winfo_y(), self.winfo_width(), self.winfo_height()
        
        print(x, y, x+w, y+h)
        
        screenshot = ImageGrab.grab(bbox=(x, y, x + w + 200, y + h + 200))
        path = filedialog.asksaveasfilename(defaultextension='.png', filetypes=[("PNG files", "*.png"), ("All Files", "*.*")])
        
        if path:
            screenshot.save(path)
        
    def toggleCamera(self):
        self.cameraRunning = not self.cameraRunning
        if self.cameraRunning:
            self.startCamera()
        else:
            self.stopCamera()
        
    def startCamera(self):
        self.cameraRunning = True
        self.videoLabel.grid_forget()
        
        self.videoLabel = tk.Label(self)
        self.videoLabel.grid(row=1, column=0, columnspan=3)
        self.webcam = cv2.VideoCapture(0)
        
        self.updateFrame()
        
    def stopCamera(self):
        self.cameraRunning = False
        self.webcam.release()
        
        self.videoLabel.grid_forget()
        message_label = tk.Label(self, text="Video camera has been turned off.")
        message_label.grid(row=1, column=0, columnspan=3)
    
    def get_tk_win_size(self):
        return self.winfo_width(), self.winfo_height()
    
    def updateFrame(self):
        if self.cameraRunning:
            _, frame = self.webcam.read()
            self.save_frame = frame
            
            tk_width, tk_height = self.get_tk_win_size()
            aspect_ratio_w = 4
            aspect_ratio_h = 3
            
            pengali = (tk_height / 3) if (tk_width > tk_height) else int(tk_width) / 4
           
            frame = cv2.resize(frame, (int(8*pengali*aspect_ratio_w/10), int(pengali*aspect_ratio_h*8/10)))
            
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

                color = (color_decider(pixel_center))
                #testing

                hex_value = rgb_to_hex(r,g,b)


                if color == "undefined":
                    self.color = ""
                else :
                    self.color = color

                self.colorframe =tk.Frame( width=70,height=40,bg=hex_value).grid(padx=50,pady=10,row=0,column=0)

                self.namacolor = tk.Frame(width =70 ,height=40).grid(padx=0,pady=10,row=0,column=1,sticky="W")
                tk.Label(self.namacolor , text=self.color,font=(50)).grid(padx=0,row=0,column=1,pady=0,sticky="W")

            
                # add square
                cv2.rectangle(frame, (cx-5, cy-5), (cx+5, cy+5), (255, 0, 0), 1)

                # add text
                cv2.putText(frame, color, (10, 50), 0, 1, (b, g, r), 2)
                # colorLabel.config(text=color)
                
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert from BGR to RGB
                image = Image.fromarray(frame)  # Create an Image object from the frame
                photo = ImageTk.PhotoImage(image=image)  # Create a PhotoImage from the Image object
                self.videoLabel.config(image=photo)  # Update the videoLabel with the new image
                self.videoLabel.image = photo  # Keep a reference to the PhotoImage to prevent garbage collection
            
                self.after(10, self.updateFrame) # Rerun updateFrame function after 10 miliseconds