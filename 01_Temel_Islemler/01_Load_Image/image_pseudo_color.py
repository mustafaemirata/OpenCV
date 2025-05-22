import cv2
import cv2 as cv

path="01_Temel_Islemler/01_Load_Image/"
src=cv.imread("images.jpeg")

#cv.namedWindow("input",cv.WINDOW_AUTOSIZE)
#cv.imshow("input",src)

#cv.waitKey(0)

#ApplyColorMap

dst=cv.applyColorMap(src,cv.COLORMAP_JET)
cv.imshow("output",dst)
cv.waitKey(0)