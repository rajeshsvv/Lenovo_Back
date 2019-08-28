
# pillow library fro python
# pillow allows us to work with and manipulate images using python
# displaying them to screen resizing them and modifying the colours and also saving them back to your screen
# this is extremely useful when u want to modify the images at a time
# install pillow


from PIL import Image, ImageFilter  # ImageFilter use is blur the image got it
import os


size_300 = (300, 300)
size_700 = (700, 700)
image_1 = Image.open("Nazria (15).jpg")
# save is for change the format like from jpg to png
# image_1.save("Nazria (27).png")

image_1.show()

# convert the image formats from jpg to png we need o import os module and save it into pillow_pngs folder k got it

# to loop over the files in the cuurent directory use os module ok got it

# for f in os.listdir("."):
#     if f.endswith(".jpg"):
#         # print(f)					 # for check purpose whether ut will show jpg pics or not ok got it
#         i = Image.open(f)
#         fn, fext = os.path.splitext(f)
#         # print(fext)					#it will show file name wise and file anem extension wise got it
#         i.save("pillow_pngs/{}.png".format(fn))  # it will add the png images to the pillow_pngs folder in the directory check it k


# resized version of all your files  for thumbnails or image galleries into pillow_300 folder k


# for f in os.listdir("."):
#     if f.endswith(".jpg"):
#         # print(f)					 # for check purpose whether ut will show jpg pics or not ok got it
#         i = Image.open(f)
#         fn, fext = os.path.splitext(f)
#         # print(fext)					#it will show file name wise and file name extension wise got it
#         i.thumbnail(size_300)
#         i.save("pillow_300/{}_300.png".format(fn, fext))

#         i.thumbnail(size_700)
#         i.save("pillow_300/{}_700.png".format(fn, fext))


# image_1 = Image.open("Nazria (27).jpg")
# save is for change the format like from jpg to png
# image_1.rotate(90).save("Nazria_27_rotate.png")  # to rotate image in 90 degrees got it
# image_1.convert(mode="L").save("Nazria_27_colour.png")
# image_1.filter(ImageFilter.GaussianBlur(15)).save("Nazria_27_blur.png")			#15 in the sense it will blur the pic more got it
