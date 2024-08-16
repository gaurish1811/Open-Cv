import cv2
img= cv2.imread('lena.jpg')
cv2.imshow('lena.jpg',img)
k=cv2.waitKey(0)
if k==27:
    cv2.destroyAllWindows()
elif k==ord('s'):
    cv2.imwrite('lena_copy.png',img)
    img2=cv2.imread("lena_copy.jpeg",1)
    cv2.imshow('lena_copy.jpeg',img2)
