from collections import deque
import serial
import numpy as np
import argparse
import imutils
import cv2
import string
import os
import math
import datetime
import time
from imutils.video import WebcamVideoStream

arduino = serial.Serial('COM3',9600)

################################################################################
##Camera Parameter 
im_widht=600
im_height=450
center_im=im_widht/2,im_height/2
camera = cv2.VideoCapture(0)


#Nilainya sama dengan HSV
Hmin = 90
Hmax = 130
Smin = 50
Smax = 255
Vmin = 70
Vmax = 255
out1 = 0


while (1):
  
        stream = cv2.waitKey(1)
        (grabbed,frame) = camera.read()
        frame = cv2.flip(frame,1)
        frame = imutils.resize(frame, width=im_widht)
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        Lower_val = np.array([Hmin,Smin,Vmin])
        Upper_val = np.array([Hmax,Smax,Vmax])
        mask = cv2.inRange(hsv, Lower_val, Upper_val)
        contours = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
        center = 1


        try :
                if len(contours) > 0:
                    cntr = max(contours, key=cv2.contourArea)
                    ((x, y), radius) = cv2.minEnclosingCircle(cntr)
                    hull = cv2.convexHull(cntr)
                    M = cv2.moments(cntr)

                    center_x = int(M["m10"] / M["m00"])
                    center_y = int(M["m01"] / M["m00"])
                    
                    mask = np.zeros(frame.shape[:2], np.uint8)
                    cv2.drawContours(frame, [hull], 0, (255,0,0) ,2)
                    cv2.rectangle(frame, (int(x) - 3, int(y) - 3), (int(x) + 3, int(y) + 3), (255, 255, 255), -1)
                    if(center_x >=1 and center_x < 200) and (center_y >1 and center_y < 150):
                       out1 = '1'
                       print('1')
                       arduino.write(out1.encode())
                    elif(center_x > 200 and center_x < 400) and (center_y >1 and center_y < 150):
                       out2 = '2'
                       print('2')
                       arduino.write(out2.encode())
                    elif(center_x > 400 and center_x < 1200) and (center_y >1 and center_y < 150):
                       out3 = '3'
                       print('3')
                       arduino.write(out3.encode())
                    elif(center_x >= 1  and center_x < 200) and (center_y >150 and center_y < 300):
                       out4 = '4'
                       print('4')
                       arduino.write(out4.encode())
                    elif(center_x > 200 and center_x < 400) and (center_y >150 and center_y < 300):
                       out5 = '5'
                       print('5')
                       arduino.write(out5.encode())
                    elif(center_x > 400 and center_x < 1200) and (center_y >150 and center_y < 300):
                       out6 = '6'
                       print('6')
                       arduino.write(out6.encode())
                    elif(center_x >= 1  and center_x < 200) and (center_y >300 and center_y < 1200):
                       out7 = '7'
                       print('7')
                       arduino.write(out7.encode())
                    elif(center_x > 200 and center_x < 400) and (center_y >300 and center_y < 1200):
                       out8 = '8'
                       print('8')
                       arduino.write(out8.encode())
                    elif(center_x > 400 and center_x < 1200) and (center_y >300 and center_y < 1200):
                       out9 = '9'
                       print('9')
                       arduino.write(out9.encode())
                    
                    else:
                        pass

                else:
                        pass
        except :
                pass
        cv2.line(img=frame, pt1=(0, 300), pt2=(4000, 300), color=(255, 255, 0), thickness=2, lineType=8, shift=1)
        cv2.line(img=frame, pt1=(0, 600), pt2=(4000, 600), color=(255, 255, 0), thickness=2, lineType=8, shift=1)
        cv2.line(img=frame, pt1=(400, 0), pt2=(400, 4500), color=(255, 255, 0), thickness=2, lineType=8, shift=1)
        cv2.line(img=frame, pt1=(850, 0), pt2=(850, 4500), color=(255, 255, 0), thickness=2, lineType=8, shift=1)
        img = imutils.resize(frame, width=1000)
        cv2.imshow('image',img)

        #print("Tengah", center)
        if stream & 0XFF == ord('q'):  #Letter 'q' is the escape key
                print("Video Berakhir")
                break 
camera.release()
cv2.destroyAllWindows()
print("Selesai")
