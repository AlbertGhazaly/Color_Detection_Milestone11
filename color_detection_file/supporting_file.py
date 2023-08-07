import cv2
import numpy as np
"""
    untuk import file dan bahan2 atau variabel2 yang akan digunain
    
"""

color_list = ["black","white","red","Red","green","blue","yellow","purple","orange","brown"]
color_dict_HSV = {'black': [[179, 255, 40], [0, 0, 0]],
              'white': [[179, 30, 255], [0, 0, 200]],
              'red': [[180, 255, 255], [159, 50, 70]],
              'Red': [[10, 255, 255], [0, 100, 100]],
              'green': [[70, 255, 255], [50, 100, 100]],
              'blue': [[130, 255, 255], [100, 100, 100]],
              'yellow': [[40, 255, 255], [20, 100, 100]],
              'purple': [[170, 255, 255], [130, 40, 40]],
              'orange': [[25, 255, 255], [10, 100, 100]],
              'brown': [[30, 255, 200], [10, 50, 40]]}

color_dict_BGR = {'black': [0,0,0],
              'white': [255,255,255],
              'red': [0,0,255],
              'Red': [0,0,255],
              'green': [0,255,0],
              'blue': [255,0,0],
              'yellow': [0,255,255],
              'purple': [128,0,128],
              'orange': [0,69,255],
              'brown':[42,42,165]
            }

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
