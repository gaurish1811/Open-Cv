# Adaptive thresholding is used to threshold images with different lighting conditions 
import cv2
img = cv2.imread("sudoku.png",0)
cv2.imshow("Sudoku",img)

#There are 2 different algorithms to do so  1) mean , 2) gausian
#These generally do not much difference in output , but somethimes one may work and other may not

#First let us see without these algo

cv2.imshow("Without algo", cv2.threshold(img,70,255,cv2.THRESH_BINARY)[1])
cv2.waitKey(0)
cv2.destroyWindow("Without algo")
#Now with algos in use
cv2.imshow("With algo",cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,11,2))
cv2.waitKey(0)
