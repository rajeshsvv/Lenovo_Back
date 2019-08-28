import cv2                      # this package is available on python package index

image=cv2.imread("Nazria.jpg",flags=1)
(h,w,d)=image.shape
print("width={},height={},depth={}".format(w,h,d))

cv2.imshow("Image",image)
cv2.waitKey(0)