# Left click gives coordinates , right click gives color in rgb 
import cv2
def Mouse(event , x , y , flag ,param):
    if event ==cv2.EVENT_LBUTTONDOWN:
        print ( x ,' , ', y)
        img = cv2.imread("lena.jpg")
        cv2.putText(img , "("+str(x) + ' , '+str(y)+")",(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),1)
        cv2.imshow("Left click",img)
    if event ==cv2.EVENT_RBUTTONDOWN:
        img = cv2.imread("lena.jpg")
        b=str(img[x,y,0])
        r=str(img[x,y,1])
        g=str(img[x,y,2])
        st1= "("+r+','+g+ ',' +b+")"
        
        cv2.putText(img ,st1,(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0),1)
        cv2.imshow("Right click",img)

img = cv2.imread("lena.jpg")
cv2.imshow("Click Here",img)
cv2.setMouseCallback("Click Here", Mouse)
cv2.waitKey(0)
