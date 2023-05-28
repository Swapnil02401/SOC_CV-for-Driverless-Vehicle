import cv2 as cv



def rescaleframe(fram,scale = 0.75):
    #works for videos , images and live videos
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    
    dimensions = (width , height)

    return cv.resize(frame , dimensions,interpolation=cv.INTER_AREA)

def changeRes(width,height):
    #works only for live videos
    capture.set(3,width)
    capture.set(4,height)

    
capture = cv.VideoCapture('catvid.mp4')    #captures the video mentioned in patht to the variable mentioned also note that VideoCapture function takes either numbers as arguments or paths only

while True:                                #while loop to display the video frame by frame
    isTrue,frame = capture.read()          #reads the capured video frame by frame , variable frame is where each frame is read into and isTrue is a boolean value which is true if the frame is read successfully
    frame_resized = rescaleframe(frame)
    
    cv.imshow('CatVideo',frame)            #displays the frames on window named CatVideo
    cv.imshow('CatVidResized',frame_resized)
    

    if cv.waitKey(20) & 0xFF==ord('d'):    #basically shuts the video if we type d
        break

capture.release()                          #releases the captured video
cv.destroyAllWindows()