import cv2 as cv

img = cv.imread('cat2.jpg')   #reads the image mentioned in path as matrix of pixels

def rescaleframe(frame,scale = 2):
    
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    
    dimensions = (width , height)

    return cv.resize(frame , dimensions,interpolation=cv.INTER_AREA)

resized_img = rescaleframe(img)

cv.imshow('ResizeCat',resized_img)    #displays the read image with window name as Cat

cv.waitKey(0)