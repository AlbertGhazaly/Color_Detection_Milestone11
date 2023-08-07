<<<<<<< HEAD:source/image_detection_v2.py
# Python code for Multiple Color Detection

from supporting_file import *


# Capturing video through webcam
webcam = cv2.VideoCapture(0)

# Start a while loop
while(1):
	
	# Reading the video from the
	# webcam in image frames
	_, imageFrame = webcam.read()

	# Convert the imageFrame in
	# BGR(RGB color space) to
	# HSV(hue-saturation-value)
	# color space
	hsvFrame = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2HSV)

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
	gray_mask = cv2.inRange(hsvFrame, np.array(color_dict_HSV["gray"][1], np.uint8), np.array(color_dict_HSV["gray"][0], np.uint8))


	# Morphological Transform, Dilation
	# for each color and bitwise_and operator
	# between imageFrame and mask determines
	# to detect only that particular color
	kernel = np.ones((5, 5), "uint8")

	# For red color
	black_mask = cv2.dilate(black_mask, kernel)
	res_black = cv2.bitwise_and(imageFrame, imageFrame,
							mask = black_mask)
	# For red color
	white_mask = cv2.dilate(white_mask, kernel)
	res_white = cv2.bitwise_and(imageFrame, imageFrame,
							mask = white_mask)
	# For red color
	red_mask = cv2.dilate(red_mask, kernel)
	res_red = cv2.bitwise_and(imageFrame, imageFrame,
							mask = red_mask)
	# For red color
	Red_mask = cv2.dilate(Red_mask, kernel)
	res_Red = cv2.bitwise_and(imageFrame, imageFrame,
							mask = Red_mask)
	# For green color
	green_mask = cv2.dilate(green_mask, kernel)
	res_green = cv2.bitwise_and(imageFrame, imageFrame,
								mask = green_mask)
	# For blue color
	blue_mask = cv2.dilate(blue_mask, kernel)
	res_blue = cv2.bitwise_and(imageFrame, imageFrame,
							mask = blue_mask)
		# For blue color
	yellow_mask = cv2.dilate(yellow_mask, kernel)
	res_yellow = cv2.bitwise_and(imageFrame, imageFrame,
							mask = yellow_mask)
	# For blue color
	purple_mask = cv2.dilate(purple_mask, kernel)
	res_purple = cv2.bitwise_and(imageFrame, imageFrame,
							mask = purple_mask)
	# For blue color
	orange_mask = cv2.dilate(orange_mask, kernel)
	res_orange = cv2.bitwise_and(imageFrame, imageFrame,
							mask = orange_mask)
	# For blue color
	gray_mask = cv2.dilate(gray_mask, kernel)
	res_gray = cv2.bitwise_and(imageFrame, imageFrame,
							mask = gray_mask)
	color_mask_list = [black_mask,white_mask,red_mask,Red_mask,green_mask,blue_mask,yellow_mask,
		    purple_mask,orange_mask,gray_mask]
	for order in range(0,10):
		# Creating contour to track red color
		contours, hierarchy = cv2.findContours(color_mask_list[order],
											cv2.RETR_TREE,
											cv2.CHAIN_APPROX_SIMPLE)

		for pic, contour in enumerate(contours):
			area = cv2.contourArea(contour)
			if(area > 300):
				x, y, w, h = cv2.boundingRect(contour)
				imageFrame = cv2.rectangle(imageFrame, (x, y),
										(x + w, y + h),
										tuple(median(color_dict_HSV[color_list[order]][1],color_dict_HSV[color_list[order]][0])), 2)
				
				cv2.putText(imageFrame, color_list[order], (x, y),
							cv2.FONT_HERSHEY_SIMPLEX, 1.0,
							tuple(median(color_dict_HSV[color_list[order]][1],color_dict_HSV[color_list[order]][0])))		
	# Program Termination
	cv2.imshow("Multiple Color Detection in Real-TIme", imageFrame)
	if cv2.waitKey(10) & 0xFF == ord('q'):
		webcam.release()
		cv2.destroyAllWindows()
=======
# Python code for Multiple Color Detection


import numpy as np
import cv2


# Capturing video through webcam
webcam = cv2.VideoCapture(0)

# Start a while loop
while(1):
	# Reading the video from the
	# webcam in image frames
	_, imageFrame = webcam.read()

	# flip image
	imageFrame = cv2.flip(imageFrame, 1)

	# Convert the imageFrame in
	# BGR(RGB color space) to
	# HSV(hue-saturation-value)
	# color space
	hsvFrame = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2HSV)

	# Set range for red color and
	# define mask
	red_lower = np.array([136, 87, 111], np.uint8)
	red_upper = np.array([180, 255, 255], np.uint8)
	red_mask = cv2.inRange(hsvFrame, red_lower, red_upper)

	# Set range for green color and
	# define mask
	green_lower = np.array([25, 52, 72], np.uint8)
	green_upper = np.array([102, 255, 255], np.uint8)
	green_mask = cv2.inRange(hsvFrame, green_lower, green_upper)

	# Set range for blue color and
	# define mask
	blue_lower = np.array([94, 80, 2], np.uint8)
	blue_upper = np.array([120, 255, 255], np.uint8)
	blue_mask = cv2.inRange(hsvFrame, blue_lower, blue_upper)
	
	# Morphological Transform, Dilation
	# for each color and bitwise_and operator
	# between imageFrame and mask determines
	# to detect only that particular color
	kernel = np.ones((5, 5), "uint8")
	
	# For red color
	red_mask = cv2.dilate(red_mask, kernel)
	res_red = cv2.bitwise_and(imageFrame, imageFrame,
							mask = red_mask)
	
	# For green color
	green_mask = cv2.dilate(green_mask, kernel)
	res_green = cv2.bitwise_and(imageFrame, imageFrame,
								mask = green_mask)
	
	# For blue color
	blue_mask = cv2.dilate(blue_mask, kernel)
	res_blue = cv2.bitwise_and(imageFrame, imageFrame,
							mask = blue_mask)

	# Creating contour to track red color
	contours, hierarchy = cv2.findContours(red_mask,
										cv2.RETR_TREE,
										cv2.CHAIN_APPROX_SIMPLE)
	
	for pic, contour in enumerate(contours):
		area = cv2.contourArea(contour)
		if(area > 300):
			x, y, w, h = cv2.boundingRect(contour)
			imageFrame = cv2.rectangle(imageFrame, (x, y),
									(x + w, y + h),
									(0, 0, 255), 2)
			
			cv2.putText(imageFrame, "Red Colour", (x, y),
						cv2.FONT_HERSHEY_SIMPLEX, 1.0,
						(0, 0, 255))	

	# Creating contour to track green color
	contours, hierarchy = cv2.findContours(green_mask,
										cv2.RETR_TREE,
										cv2.CHAIN_APPROX_SIMPLE)
	
	for pic, contour in enumerate(contours):
		area = cv2.contourArea(contour)
		if(area > 300):
			x, y, w, h = cv2.boundingRect(contour)
			imageFrame = cv2.rectangle(imageFrame, (x, y),
									(x + w, y + h),
									(0, 255, 0), 2)
			
			cv2.putText(imageFrame, "Green Colour", (x, y),
						cv2.FONT_HERSHEY_SIMPLEX,
						1.0, (0, 255, 0))

	# Creating contour to track blue color
	contours, hierarchy = cv2.findContours(blue_mask,
										cv2.RETR_TREE,
										cv2.CHAIN_APPROX_SIMPLE)
	for pic, contour in enumerate(contours):
		area = cv2.contourArea(contour)
		if(area > 300):
			x, y, w, h = cv2.boundingRect(contour)
			imageFrame = cv2.rectangle(imageFrame, (x, y),
									(x + w, y + h),
									(255, 0, 0), 2)
			
			cv2.putText(imageFrame, "Blue Colour", (x, y),
						cv2.FONT_HERSHEY_SIMPLEX,
						1.0, (255, 0, 0))
			
	# Program Termination
	cv2.imshow("Multiple Color Detection in Real-TIme", imageFrame)
	if cv2.waitKey(10) & 0xFF == ord('q'):
		webcam.release()
		cv2.destroyAllWindows()
>>>>>>> main:color_detection_file/image_detection_v2.py
		break