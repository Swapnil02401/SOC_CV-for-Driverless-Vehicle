import cv2 as cv
import numpy as np

img = cv.imread('cat2.jpg')   #reads the image mentioned in path as matrix of pixels

cv.imshow('Cat',img)    #displays the read image with window name as Cat

#translation

def translate(img,x,y):
    transmat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1],img.shape[0])
    return cv.warpAffine(img,transmat,dimensions)

#-x > left
#x > right
#-y > up
#y > down
translated = translate(img,-75,75)
cv.imshow('Translated image',translated)

#Rotation
'''
def rotate(img,angle,rotPoint = None):
    (height,width) = img[:2]
    if rotPoint is None:
        rotPoint = (width//2,height//2)

    rotMat =  cv.getRotationMatrix2D(rotPoint,angle,1.0)
    dimensions = (width,height)
    return cv.warpAffine(img,rotMat,dimensions)

rotated = rotate(img,45)
cv.imshow('rotatedimg',rotated)
'''

#flipping
flip = cv.flip(img,-1)
cv.imshow('flippedimg',flip)
# 0 for vertical flip
# 1 for horizontal flip
#-1 for vert and horz flip

cv.waitKey(0)