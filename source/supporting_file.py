import cv2
import numpy as np
"""
    untuk import file dan bahan2 atau variabel2 yang akan digunain
    
"""

def color_decider(hue_value):
    color = "undefined"
    if hue_value < 5:
        color = "RED"
    elif hue_value < 22:
        color = "ORANGE"
    elif hue_value < 33:
        color = "YELLOW"
    elif hue_value < 78:
        color = "GREEN"
    elif hue_value < 131:
        color = "BLUE"
    elif hue_value < 170:
        color = "VIOLET"
    else:
        color = "RED"

    return color
