import cv2

cv2.namedWindow("Preview")
cap = cv2.VideoCapture(0)


rval, frame = cap.read()

cv2.imshow('Preview', frame)

# time for which image displayed
cv2.waitKey(3000)

name = input("Enter file name: ")

# Save the frame
cv2.imwrite(name + '.jpg', frame)

