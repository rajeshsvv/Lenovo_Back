import cv2

# Balck and White Gray Scale
img=cv2.imread("Nazria.jpg",1)
# img_1=cv2.imread("Nazria.jpg",1)


# print(img.axis)
# print(img.head())
# print(type(img))
# print(img[1])
print(img.shape)

# open and resize the image
resize_image=cv2.resize(img,(int(img.shape[1]/2),int(img.shape[1]/2)))
cv2.imshow("Nazria.jpg",resize_image)
cv2.imshow("Nazria.img",img)
cv2.waitKey()
cv2.destroyAllWindows()
cv2.imwrite("Nazria_resize.jpg",resize_image)
