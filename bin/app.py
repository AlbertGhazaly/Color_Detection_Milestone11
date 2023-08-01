import os
import sys
import cv2
import tkinter as tk
from PIL import Image, ImageTk

# Get the parent directory of your current directory
parentdir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Create the absolute path of the sibling directory
siblingPath = os.path.join(parentdir, "src")

# Add the sibling directory to the sys.path list
sys.path.append(siblingPath)

# Import module from sibling directory
from supporting_file import *

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
        
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert from BGR to RGB
        image = Image.fromarray(frame)  # Create an Image object from the frame
        photo = ImageTk.PhotoImage(image=image)  # Create a PhotoImage from the Image object
        label.config(image=photo)  # Update the label with the new image
        label.image = photo  # Keep a reference to the PhotoImage to prevent garbage collection
    
    root.after(10, updateFrame) # Rerun updateFrame function after 10 miliseconds

root = tk.Tk()
root.title("Webcam Display")

label = tk.Label(root)
label.pack()

webcam = cv2.VideoCapture(0)  # 0 for the default camera (change to 1 for an external camera)
updateFrame()

root.mainloop()

webcam.release()  # Release the webcam