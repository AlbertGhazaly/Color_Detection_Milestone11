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
	brown_mask = cv2.inRange(hsvFrame, np.array(color_dict_HSV["brown"][1], np.uint8), np.array(color_dict_HSV["brown"][0], np.uint8))
	


	# Morphological Transform, Dilation
	# for each color and bitwise_and operator
	# between imageFrame and mask determines
	# to detect only that particular color
	kernel = np.ones((5, 5), "uint8")

	#Create mask and implementation for each color in image

	# For black color
	black_mask = cv2.dilate(black_mask, kernel)
	res_black = cv2.bitwise_and(imageFrame, imageFrame,
							mask = black_mask)
	# For white color
	white_mask = cv2.dilate(white_mask, kernel)
	res_white = cv2.bitwise_and(imageFrame, imageFrame,
							mask = white_mask)
	# For red color
	red_mask = cv2.dilate(red_mask, kernel)
	res_red = cv2.bitwise_and(imageFrame, imageFrame,
							mask = red_mask)
	# For Red color
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
	# For yellow color
	yellow_mask = cv2.dilate(yellow_mask, kernel)
	res_yellow = cv2.bitwise_and(imageFrame, imageFrame,
							mask = yellow_mask)
	# For purple color
	purple_mask = cv2.dilate(purple_mask, kernel)
	res_purple = cv2.bitwise_and(imageFrame, imageFrame,
							mask = purple_mask)
	# For blue color
	orange_mask = cv2.dilate(orange_mask, kernel)
	res_orange = cv2.bitwise_and(imageFrame, imageFrame,
							mask = orange_mask)
	# For brown color
	brown_mask = cv2.dilate(brown_mask, kernel)
	res_brown = cv2.bitwise_and(imageFrame, imageFrame,
							mask = brown_mask)
	

	# list of colors
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
				x, y, w, h = cv2.boundingRect(contour) #the rectangle
				imageFrame = cv2.rectangle(imageFrame, (x, y),
			       						(x + w, y + h),
				  						 tuple(color_dict_BGR[color_list[order]]), 2)
				#Puting text on rectangle
				cv2.putText(imageFrame, color_list[order], (x, y),
							cv2.FONT_HERSHEY_SIMPLEX, 1.0,
							tuple(color_dict_BGR[color_list[order]]))		
				
	# Program Termination
	cv2.imshow("Multiple Color Detection in Real-TIme", imageFrame)
	key = cv2.waitKey(1)
	if key == 27: # press 'esc'
		break