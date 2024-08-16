import cv2
cap = cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH) , cap.get(cv2.CAP_PROP_FRAME_HEIGHT) )

# Change resolulution
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH) , cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

i=0
while True:
    i+=8
#Convert to grayscale but store as colour
    ret, frame = cap.read()
    cv2.imwrite("Gray.jpg",frame)
    frame= cv2.imread("Gray.jpg",0)
    cv2.imwrite("Gray.jpg",frame)
    frame= cv2.imread("Gray.jpg")

#Write Akshansh on top
    frame=cv2.putText(frame,'Akshansh',(1280//2,30),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,i//2,255-i),1)
    k=cv2.waitKey(1)
    if k!=-1:                       #Press any key to escape
        break
    cv2.imshow('Camera', frame)
    if i>=255:
        i=0
cap.release()
cv2.destroyAllWindows()
