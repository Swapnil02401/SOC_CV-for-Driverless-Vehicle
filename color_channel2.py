import cv2 as cv
import numpy as np

img = cv.imread('cat_large.jpg')   # reads the image mentioned in path as a matrix of pixels

b, g, r = cv.split(img)  # splitting the 3 color channels

# Create blank images for blue and green channels
blank = np.zeros_like(b)

blue = cv.merge([b, blank, blank])   # set red and green channels to blank
green = cv.merge([blank, g, blank])  # set blue and red channels to blank
red = cv.merge([blank, blank, r])    # set blue and green channels to blank

cv.imshow('Blue', blue)
cv.imshow('Green', green)
cv.imshow('Red', red)

cv.waitKey(0)

