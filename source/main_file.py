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
        print(cx, cy)
        
        # pick pixel value
        pixel_center = hsv_frame(cy, cx)
        print(f"pixel center - {pixel_center}")
        # add square
        cv2.square(frame, (cx, cy), 5, (255, 0, 0), 3)
        
        # show video per frame
        cv2.imshow("Frame", frame)

        key = cv2.waitKey(1)
        if key == 27: # press 'esc'
            break

    cap.release()
    cv2.destroyAllWindows()
    
    

if __name__ == "__main__":
    main()
