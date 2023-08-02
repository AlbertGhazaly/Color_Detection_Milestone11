import os
import sys
import cv2
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from PIL import Image, ImageTk

from color_detection_file.supporting_file import *

class App(tk.Tk):

    def __init__(self):
        super().__init__()

        # camera
        self.videoLabel = tk.Label(self)
        self.videoLabel.pack()
        self.webcam = cv2.VideoCapture(0)
        self.updateFrame()
        
        # tombol
        self.button = ttk.Button(self, text='Click Me')
        self.button['command'] = self.button_clicked
        self.button.pack()

    # bisa juga bikin fungsi baru.
    def button_clicked(self):
        showinfo(title="information", message="hello")
    
    def updateFrame(self):
        _, frame = self.webcam.read()
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

app = App()
app.mainloop()