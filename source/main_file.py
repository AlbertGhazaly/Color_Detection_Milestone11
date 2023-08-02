from supporting_file import *

def main():
    # main code
    
    cap = cv2.VideoCapture(0)
    while True:
        _, frame = cap.read()
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
        
        # show video per frame
        cv2.imshow("Frame", frame)
        
        key = cv2.waitKey(1)
        if key == 27: # press 'esc'
            break
    
    

if __name__ == "__main__":
    main()
