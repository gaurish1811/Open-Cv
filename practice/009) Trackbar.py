import cv2
import numpy as np

img =np.zeros((512,512,3),np.uint8)
cv2.imshow("Image",img)
b=g=r=0
def nothing(x):
    b=x
cv2.createTrackbar("B","Image",0,255,nothing)
cv2.createTrackbar("G","Image",0,255,nothing)
cv2.createTrackbar("R","Image",0,255,nothing)
cv2.createTrackbar("Switch","Image",0,1,nothing)
while (1):
    b=cv2.getTrackbarPos("B","Image")
    g=cv2.getTrackbarPos("G","Image")
    r=cv2.getTrackbarPos("R","Image")
    s=cv2.getTrackbarPos("Switch","Image")
    if s:
       img[:]=[b,g,r]
    else:
        pass
    cv2.imshow("Image",img)
    k=cv2.waitKey ( 100 )
    if k==27:
        break
