import cv2 as cv

# If twitter.png is in the same directory as this script, just use the filename
img = cv.imread("twitter.png")

print(type(img))
cv.namedWindow("opencv_test", cv.WINDOW_AUTOSIZE)  # orijinal boyutta olmasını sağlar.

# imshow (resimleri göstermek için)
cv.imshow("opencv_test", img)
cv.waitKey(6000)

#Bütün pencereleri kapatmak için kullandık.
cv.destroyAllWindows()


