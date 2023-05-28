import cv2 as cv
import numpy as np

img = cv.imread('cat_large.jpg')   #reads the image mentioned in path as matrix of pixels

cv.imshow('Cat',img)    #displays the read image with window name as Cat
blank = np.zeros(img.shape,dtype='uint8')

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('GRAY',gray)
'''
blur = cv.blur(gray,(5,5),cv.BORDER_DEFAULT)
cv.imshow('blurred',blur)
'''
canny = cv.Canny(img,125,175)

cv.imshow('canny',canny)

ret , thresh = cv.threshold(gray,125,255,cv.THRESH_BINARY)

cv.imshow('Thresh',thresh)

countours,hierarchies  = cv.findContours(thresh,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)

cv.drawContours(blank,countours,-1,(0,0,255),1)
cv.imshow('countours drawn',blank)

print(len(countours))
cv.waitKey(0)