import numpy as np #numpy
import cv2  #opencv
import serial #pyserial

usbport = 'COM16'   #The port to which arduino is connected to

ser = serial.Serial(usbport, 9600, timeout=1)

face_cascade = cv2.CascadeClassifier('D:\opencv\sources\data\haarcascades\haarcascade_frontalface_default.xml') #Path of the haarcascade_frontalface_default file

img = cv2.VideoCapture(1)

angle = 90  #Initial angle the servo is at


while(True):
    ret, frame = img.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  #The frame has to be in gray mode for the video to be processed
    faces = face_cascade.detectMultiScale(gray, 1.3, 5) #Tweak these values for it to detect properly. You may need to change these values if the lighting changes
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        center_point = ((x+(x+w))/2, (y+(y+h))/2)
        cv2.rectangle(frame, center_point, center_point, (255, 0, 0), 2)

        #The values 50 and 600 are the boundaries of the rectangle formed by the detection of faces 
        #which if it exceeds would trigger the servo to change its angle accordingly. 

        if(x <= 50):
            angle += 5
            ser.write(str(angle) + '\n')

        if((x+w) >= 600):
            angle -= 5
            ser.write(str(angle) + '\n')

    cv2.imshow('img', frame)
    if cv2.waitKey(25) == 27:   #27 is the ASCII value of ESC key. 
        break                          

cv2.destroyAllWindows()
img.release()
