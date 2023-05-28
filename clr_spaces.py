import cv2 as cv
#import matplotlib.pyplot as plt

img = cv.imread('cat_large.jpg')   #reads the image mentioned in path as matrix of pixels

cv.imshow('Cat',img)    #displays the read image with window name as Cat

#plt.imshow(img)
#plt.show()     #inversion of colors from BGR to RGB

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY) # BGR to Gray

#BGR to HSV

hsv_img = cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('HSV',hsv_img)

#BGR to LAB

lab_img = cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow('lab',lab_img)

#BGR to RGB color inversion method 2

rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB',rgb)

#we cannot conver gray scale img to hsv directly we need to first convert it to BGR then to HSV

#HSV to BGR

hsv_bgr = cv.cvtColor(hsv_img,cv.COLOR_HSV2BGR)
cv.imshow('HSV2BGR',hsv_bgr)

#similarly we can convert LAB to BGR and Gray to BGR

cv.waitKey(0)