import cv2
img = cv2.imread("lena.jpg")
img2= cv2.imread("messi.jpg")
img=cv2.resize(img,(512,512))
img2=cv2.resize(img2,(512,512))
img=cv2.addWeighted(img,0.4 ,img2,0.9,20)
cv2.imshow("combined",img)
cv2.waitKey(0)
