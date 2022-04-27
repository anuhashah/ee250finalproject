import cv2
import time

TIMER = int(3)

cv2.namedWindow("Press Spacebar to Take Picture")
cap = cv2.VideoCapture(0)

while True:
     
    # Read and display each frame
    rval, frame = cap.read()
    cv2.imshow('Press Spacebar to Take Picture', frame)
 
    # check for the key pressed
    key = cv2.waitKey(125)

    if key == ord(' '):
            prev = time.time()
     
            while TIMER >= 0:
                rval, frame = cap.read()
     
                # Display countdown on each frame
                # specify the font and draw the
                # countdown using puttext
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(frame, str(TIMER),
                            (200, 250), font,
                            7, (0, 255, 255),
                            4, cv2.LINE_AA)
                cv2.imshow('Preview', rval)
                cv2.waitKey(125)
     
                # current time
                cur = time.time()

                # Update and keep track of Countdown
                # if time elapsed is one second
                # than decrease the counter
                if cur-prev >= 1:
                    prev = cur
                    TIMER = TIMER-1
     
            else:
                rval, frame = cap.read()
     
                # Display the clicked frame for 2
                # sec.You can increase time in
                # waitKey also
                cv2.imshow('Preview', frame)
     
                # time for which image displayed
                cv2.waitKey(2000)
     
                # Save the frame
                cv2.imwrite('camera.png', frame)
     
                # HERE we can reset the Countdown timer
                # if we want more Capture without closing
                # the camera

    # Press Esc to exit
    elif key == 27:
        break