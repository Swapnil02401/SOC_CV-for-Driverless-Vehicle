import cv2 as cv

capture = cv.VideoCapture('catvid.mp4')    #captures the video mentioned in patht to the variable mentioned

while True:                                #while loop to display the video frame by frame
    isTrue,frame = capture.read()          #reads the capured video frame by frame , variable frame is where each frame is read into and isTrue is a boolean value which is true if the frame is read successfully
    cv.imshow('CatVideo',frame)            #displays the frames on window named CatVideo

    if cv.waitKey(20) & 0xFF==ord('d'):    #basically shuts the video if we type d
        break

capture.release()                          #releases the captured video
cv.destroyAllWindows()