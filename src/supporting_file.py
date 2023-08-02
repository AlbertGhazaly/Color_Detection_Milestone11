import cv2
import numpy as np

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
