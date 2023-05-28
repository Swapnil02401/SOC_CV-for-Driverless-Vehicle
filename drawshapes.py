import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3),dtype='uint8')  #creating a dummy blank image that we can work with of size 500x500 and 3 colour chanells 
cv.imshow('Blankimg',blank)

#img = cv.imread('cat2.jpg')   
#cv.imshow('Cat',img)

# 1. Paint the blank image green
#blank[:] = 0,255,0          #0,255,0 is green code, 0,0,255 is red code, 255,0,0 is blue code

#cv.imshow('Green',blank)

#2.Draw a rectangle


#cv.rectangle(blank,(0,0),(250,250),(255,0,0),thickness=3) #blue rectangle on blank with mentioned coordinates with thickness of 3
#cv.rectangle(blank,(0,0),(250,250),(255,0,0),thickness=cv.FILLED) #fills the rectangle with that colour we can use -1 instead pf cv.FILLED we would get the same result

# Another method to draw rectangle
cv.rectangle(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(255,0,0),thickness = -1)

# 3. Draw a circle

cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),40,(0,0,255),thickness = -1)

# 4. Draw a line
cv.line(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(255,255,255),thickness=3)

# 5. Write text
cv.putText(blank,'hello',(220,220),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,255,0),2)
cv.imshow('rectbalnk',blank)

cv.waitKey(0)

