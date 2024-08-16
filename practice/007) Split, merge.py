#Display a RGB image in other all 27 colour patterns:-( (r,r,r) , (r,r,g) (r,r,b) ,....(b,b,b) )
import cv2 
img = cv2.imread("lena.jpg")
print("Shape is ",img.shape,"\n")
print("Size is ",img.size, "\n")
print("Data type is ",img.dtype,"\n")
b ,g,r =cv2.split(img)
print(img)
a,a1=[r,g,b],['r','g','b']
for i in range(0,3):
    for j in range(0,3):
        for k in range(0,3):

            cv2.imshow(str(a1[i])+str(a1[j])+str(a1[k]),cv2.merge((a[k],a[j],a[i])))
cv2.waitKey(0)
