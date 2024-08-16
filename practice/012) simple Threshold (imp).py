#See Threshold explain.png for better understanding different technique
import cv2
import random as rd
img=cv2.imread("gradient.png",0)
cv2.imshow("g",img)
_,I1=cv2.threshold(img,190,200,cv2.THRESH_BINARY)
'''
cv2.THRESH_BINARY gives output 0
cv2.THRESH_BINARY_INV       -> 1
TRUNC                       -> 2
TOZERO                      -> 3
TOZERO INV                  -> 4
MASK                        -> 5
OTSU                        -> 6
TRIANGLE                    -> 7
'''
dict = {'BINARY': 0,'BINARY INV': 1,'TRUNC': 2,'TOZERO': 3,'TOZERO INV': 4,'MASK': 5,'OTSU': 6,'TRIANGLE': 7}
#Not perfect example of mask , otsu ,triangle
a= rd.randint(0,256)
b=rd.randint(a,256)
for key in dict:
    cv2.imshow(key,cv2.threshold(img,a,b,dict[key])[1])
    print(key,cv2.threshold(img,a,b,dict[key])[1])

cv2.waitKey(0)
