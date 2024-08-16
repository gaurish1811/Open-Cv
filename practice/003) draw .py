import cv2
#Draw a colored line on grayscale image 

#Stores bgr image as Grayscale
img = cv2.imread('lena.jpg',0)
cv2.imwrite('Lena Copy.jpg', img)
img=cv2.imread('Lena Copy.jpg')

#Draw a line on the image
img= cv2.line(img, (0,0), (400,300), (255,0,0) ,50)
cv2.imshow("Line",img)
cv2.waitKey(0)
cv2.destroyWindow("Line")


# Draw an arrowed line on same image
img = cv2.arrowedLine(img, (100,200), (400,300), (0,255,0) , 20)
cv2.imshow("Line",img)
cv2.waitKey(0)
cv2.destroyWindow("Line")


#Draw a color changing rectangle
i=0
while True:
    img = cv2.rectangle(img, (100,100), (300,300), (i,255-i,i//2) , 20)
    cv2.imshow("Rectangle",img)
    k = cv2.waitKey(1)
    if i<255:
        i+=1
    else:
        i=0
    if k == 27:
        break
cv2.destroyWindow("Rectangle")

#Draw a circle (filled)

img = cv2.imread("Lena Copy.jpg")
img = cv2.circle(img , (300,280) , 130 , (255,16,173) , -1) # to fill enter thickness =-1
cv2.imshow('Circle' ,img)
cv2.waitKey(0)

# Write text 
font =cv2.FONT_HERSHEY_DUPLEX
size =0.7
cv2.putText(img , "Inappropiate Face" , (200,280) ,font, size , (0,239,82) , 1 , cv2.LINE_AA) #Line type is optional in all above too
cv2.imshow('Circle' ,img)
cv2.waitKey(0)
