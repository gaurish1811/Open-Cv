# Connect points from mouse
import cv2
def click(event,x,y,flag,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x,y),3,(255,0,0),-1)
        points.append((x,y))
        if len(points)>=2:
            cv2.line(img,points[-2],points[-1],(255,0,0),3)
            cv2.imshow('lena.jpg',img)
points=[]
img=cv2.imread("lena.jpg")
cv2.imshow("lena.jpg",img)
cv2.setMouseCallback("lena.jpg",click)
cv2.waitKey(0)
