import cv2 as cv

img = cv.imread('senery.jpg')   #reads the image mentioned in path as matrix of pixels

cv.imshow('senery',img)    #displays the read image with window name as Cat

#converting our image to grayscale 

#gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#cv.imshow('Catgry',gray)

#blur

blur = cv.GaussianBlur(img,(15,15),cv.BORDER_DEFAULT)  #(odd,odd) tells how much to blur
cv.imshow('Blur',blur)

#Edges canned

canny = cv.Canny(blur,5,75)
cv.imshow('Edges',canny)

# Dilating the image
dialated = cv.dilate(canny,(7,7),iterations =2)
cv.imshow('dilatedimg',dialated)

#eroding
erode = cv.erode(dialated,(7,7),iterations = 2)
cv.imshow('erodedimg',erode)

#Resize img

resize = cv.resize(img,(500,500),interpolation=cv.INTER_LINEAR) #in interpolation we can use cv.INTER_CUBIC,cv.INTER_LINEAR when we are converting to larger image and cv.INTER_AREA if we are converting to smaller image
cv.imshow('Resized img',resize)

#Cropping of image

crop = img[50:200,200:400]
cv.imshow('croppedimg',crop)

cv.waitKey(0)