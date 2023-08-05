import os
import sys
import cv2
import numpy as np
import tkinter as tk
from PIL import Image, ImageTk

# color dictionary HSV (upper range, lower range)
color_dict_HSV = {'black': [[180, 255, 30], [0, 0, 0]],
              'white': [[180, 18, 255], [0, 0, 231]],
              'red1': [[180, 255, 255], [159, 50, 70]],
              'red2': [[9, 255, 255], [0, 50, 70]],
              'green': [[89, 255, 255], [36, 50, 70]],
              'blue': [[128, 255, 255], [90, 50, 70]],
              'yellow': [[35, 255, 255], [25, 50, 70]],
              'purple': [[158, 255, 255], [129, 50, 70]],
              'orange': [[24, 255, 255], [10, 50, 70]],
              'gray': [[180, 18, 230], [0, 0, 40]]}

# To determine the color using HSV
def color_decider(pixel):
    hue_value = pixel[0]
    saturation_value = pixel[1]
    light_value = pixel[2]
    color = "undefined"
    for colour in color_dict_HSV:
        if ((color_dict_HSV[colour][1][0]<= hue_value and color_dict_HSV[colour][0][0]>= hue_value) and 
            (color_dict_HSV[colour][1][1]<= saturation_value and color_dict_HSV[colour][0][1]>=saturation_value) and
            (color_dict_HSV[colour][1][2]<= light_value and color_dict_HSV[colour][0][2]>=light_value)):
            color = colour
            
    return color

def updateFrame():
    _, frame = webcam.read()
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
        colorLabel.config(text=color)
        
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert from BGR to RGB
        image = Image.fromarray(frame)  # Create an Image object from the frame
        photo = ImageTk.PhotoImage(image=image)  # Create a PhotoImage from the Image object
        videoLabel.config(image=photo)  # Update the videoLabel with the new image
        videoLabel.image = photo  # Keep a reference to the PhotoImage to prevent garbage collection
    
    root.after(10, updateFrame) # Rerun updateFrame function after 10 miliseconds

root = tk.Tk()
root.title("Color Detection App")

videoLabel = tk.Label(root)
videoLabel.grid(row=0, column=0)

colorLabel = tk.Label(root, text="Color")
colorLabel.grid(row=1, column=0)

entry = tk.Entry(root)
entry.grid(row=1, column=1)

webcam = cv2.VideoCapture(0)  # 0 for the default camera (change to 1 for an external camera)
updateFrame()

root.mainloop()

webcam.release()  # Release the webcam