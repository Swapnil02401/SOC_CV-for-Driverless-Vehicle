import cv2 as cv

img = cv.imread('cat_large.jpg')   #reads the image mentioned in path as matrix of pixels

cv.imshow('Cat',img)    #displays the read image with window name as Cat

cv.waitKey(0)