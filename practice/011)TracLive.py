import cv2
import numpy as np

def a(x):
    pass

cap = cv2.VideoCapture(0);

cv2.namedWindow("Slider")
cv2.createTrackbar("LH", "Slider", 0, 255, a)
cv2.createTrackbar("LS", "Slider", 0, 255, a)
cv2.createTrackbar("LV", "Slider", 0, 255, a)
cv2.createTrackbar("UH", "Slider", 255, 255, a)
cv2.createTrackbar("US", "Slider", 255, 255, a)
cv2.createTrackbar("UV", "Slider", 255, 255, a)

while True:
    rtd, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    l_h = cv2.getTrackbarPos("LH", "Slider")
    l_s = cv2.getTrackbarPos("LS", "Slider")
    l_v = cv2.getTrackbarPos("LV", "Slider")

    u_h = cv2.getTrackbarPos("UH", "Slider")
    u_s = cv2.getTrackbarPos("US", "Slider")
    u_v = cv2.getTrackbarPos("UV", "Slider")

    l_b = np.array([l_h, l_s, l_v])
    u_b = np.array([u_h, u_s, u_v])

    mask = cv2.inRange(hsv, l_b, u_b)

    res = cv2.bitwise_and(frame, frame, mask=mask)
# 
    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("res", res)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
