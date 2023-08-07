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

from color_detection_file.supporting_file import *

class App2(tk.Frame):
    def __init__(self, parent, show_page_callback):
        super().__init__(parent)
        self.show_page_callback = show_page_callback
        
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
        yMode = 16

        tk.Label(self,text="Multi Color").place(x=600, y= yMode)
        tk.Label(self,text="Detection").place(x=600, y= yMode + 27)
        
        # Camera Section
        self.cameraTop = 110
        self.canvas.create_rectangle(115, self.cameraTop, 608, 470, outline = "light grey", fill="light grey")
        
        self.videoLabel = tk.Label(self)
        self.videoLabel.place(x=145, y=self.cameraTop)
        self.webcam = cv2.VideoCapture(0)
                
        # Camera Footer
        # width, height = 433, 325
        # camera bottom y = 415
        select = self.canvas.create_text(528,yMode+7,text='Mode:', font='Aerial 14 bold', tags='select-button')
        back = self.canvas.create_text(190, self.cameraTop + 343, text='Back', font='Aerial 12', tags='back-button')
        screenshot = self.canvas.create_text(335, self.cameraTop + 343, text='Screenshot', font='Aerial 12')
        toggle = self.canvas.create_text(510, self.cameraTop + 343, text='Toggle Camera', font='Aerial 12', tags= 'toggle-camera')
        
        # Add underline to buttons
        bboxBack = self.canvas.bbox(back)
        bboxScreenshot = self.canvas.bbox(screenshot)
        bboxToggle = self.canvas.bbox(toggle)
        
        self.canvas.create_rectangle(bboxBack[0], bboxBack[3], bboxBack[2], bboxBack[3] + 1, outline='red', fill = 'red')
        self.canvas.create_rectangle(bboxScreenshot[0], bboxScreenshot[3], bboxScreenshot[2], bboxScreenshot[3] + 1, outline='green', fill = 'green')
        self.canvas.create_rectangle(bboxToggle[0], bboxToggle[3], bboxToggle[2], bboxToggle[3] + 1, outline='blue', fill = 'blue')
        
        # select mode
        self.canvas.tag_bind('select-button','<Button-1>',self.select_mode)
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
    
    def select_mode(self,event):
        self.show_page_callback('page5')