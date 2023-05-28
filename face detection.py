import cv2 as cv

img = cv.imread('multiface.jpeg')  

cv.imshow('Faces',img)    

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

haar_cascade = cv.CascadeClassifier('haar_face.xml') #reading the haar_face file

faces_rect = haar_cascade.detectMultiScale(gray,scaleFactor = 1.1 , minNeighbors = 3)

print(len(faces_rect))

for (x,y,w,h) in faces_rect:
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness = 2)

cv.imshow('Detected faces',img)

cv.waitKey(0)