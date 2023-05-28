import cv2 as cv
import numpy as np

img = cv.imread('cat_large.jpg')   # reads the image mentioned in path as a matrix of pixels
blank = np.zeros(img.shape, dtype='uint8')

cv.imshow('Cat', img)    # displays the read image with the window name as "Cat"

b, g, r = cv.split(img)  # splitting the 3 color channels
blue = cv.merge([b, blank, blank])   # red and green set to blank
red = cv.merge([blank, blank, r])
green = cv.merge([blank, g, blank])

cv.imshow('Blue', blue)
cv.imshow('Green', green)
cv.imshow('Red', red)
print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

# merging the color channels
merged = cv.merge([b, g, r])

cv.imshow('Merged_img', merged)

cv.waitKey(0)
