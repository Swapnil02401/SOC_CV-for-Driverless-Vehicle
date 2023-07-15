import cv2 as cv
import numpy as np

cap = cv.VideoCapture("Cars3.mp4")
net = cv.dnn.readNetFromONNX("yolov5n.onnx")
file = open("coco.txt","r")
classes = file.read().split('\n')
print(classes)

while True:
    isTrue,img = cap.read()
    img = cv.resize(img,(1000,600))
    

    blob = cv.dnn.blobFromImage(img,scalefactor=1/255,size = (640,640),mean = (0,0,0),swapRB=True,crop = False)
    net.setInput(blob)
    detection = net.forward()[0]
    print(detection.shape)

    classes_ids = []
    confidences = []
    boxes = []
    rows = detection.shape[0]
    
    img_width,img_height = img.shape[1],img.shape[0]
    x_scale = img_width/640
    y_scale = img_height/640

    for i in range(rows):
        row = detection[i]
        confidence = row[4]
        if confidence > 0.5:
            classes_score = row[5:]
            ind = np.argmax(classes_score)
            if classes_score[ind]>0.5:
                classes_ids.append(ind)
                confidences.append(confidence)
                cx,cy,w,h = row[:4]
                x1 = int((cx- w/2)*x_scale)
                y1 = int((cy-h/2)*y_scale)
                width = int(w*x_scale)
                height = int(h*y_scale)
                box = np.array([x1,y1,width,height])
                boxes.append(box)
    
    for i in range(len(boxes)):
        x1,y1,w,h = boxes[i]
        label = classes[classes_ids[i]]
        conf = confidences[i]
        text = label +"{:.2f}".format(conf)
        cv.rectangle(img,(x1,y1),(x1+w,y1+h),(255,0,0),2)
        cv.putText(img,text,(x1,y1-2),cv.FONT_HERSHEY_COMPLEX,0.7,(255,0,255),2)
    cv.imshow("Vid",img)

    if cv.waitKey(10) & 0xFF==ord('d'):
        break
    
    

