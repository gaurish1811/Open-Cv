import cv2
def nothing(x):
    pass
cap = cv2.VideoCapture(0)
cv2.namedWindow("Camera")
cv2.createTrackbar("Max","Camera",0,255,nothing)
cv2.createTrackbar("Block Size","Camera",11,255,nothing)
cv2.createTrackbar("C","Camera",2,255,nothing)
while 1:
    _,frame=cap.read()
    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    max=cv2.getTrackbarPos("Max","Camera")
    Block_Size=cv2.getTrackbarPos("Block Size","Camera")
    if Block_Size%2==0:
        Block_Size+=1
    C=cv2.getTrackbarPos("C","Camera")
    frame=cv2.adaptiveThreshold(frame,max,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,Block_Size,C)
    cv2.imshow("Camera",frame)
    if cv2.waitKey(1)==27:
        break