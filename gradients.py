import cv2 as cv
import numpy as np

img = cv.imread('cat_large.jpg')   #reads the image mentioned in path as matrix of pixels

cv.imshow('Cat',img)    #displays the read image with window name as Cat

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Grayscale',gray)

#Laplacian

lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian',lap)

#Sobel
sobel_x = cv.Sobel(gray,cv.CV_64F,1,0)
sobel_y = cv.Sobel(gray,cv.CV_64F,0,1)
cv.imshow('SobleX',sobel_x)
cv.imshow('SobleY',sobel_y)
combined_sobel = cv.bitwise_or(sobel_x,sobel_y)
cv.imshow('Combined Sobel',combined_sobel)


canny = cv.Canny(gray,150,175)  #more complex gradient method which uses sobel in its intermeditate steps
cv.imshow('Canned',canny)

cv.waitKey(0)