import cv2 as cv

img = cv.imread('cat_large.jpg')   #reads the image mentioned in path as matrix of pixels

cv.imshow('Cat',img)    #displays the read image with window name as Cat

#Averaging
average = cv.blur(img,(3,3)) #(3,3) represents the kernel size , it creates a kernel in which the blur amount of the center square is the average of the blur of the surrounding sq blurt therefore kernel size should be odd only.
cv.imshow('Average Blur',average)

#Gaussian blur gives less blur than averaging blur but is more natural blur than average blur
gauss = cv.GaussianBlur(img,(3,3),0)
cv.imshow('Gaussian blur',gauss)

#Median blur same as averaging but instead of average it finds median ,better than the previous two techniques
median = cv.medianBlur(img,3) # no need to give tuple for size just an odd integer is enough
cv.imshow('Median blur',median)

#Billateral blurring is most effective blurring technique , blurred image but has edges retained
billat = cv.bilateralFilter(img,5,15,15) # 5 represents diameter , 1st 15 is sigmacolor which tells how many surrounding cours to take into consideration while blurring, 2nd 15 represents sigma space which tells till what distance from current pixel it should consider to affect the current pixels blurring
cv.imshow('Billateral blur',billat)
cv.waitKey(0)