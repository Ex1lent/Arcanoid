# выделение цвета с помощью opencv на видео

import cv2
import numpy as np
import serial
import time

arduinoSerial = serial.Serial('COM8', 9600) #указать нужный COM
time.sleep(3)

#width = 640
#heigth = 480
cap = cv2.VideoCapture(1) #указываем нужную камеру
#cap.set(3, width)
#cap.set(4, heigth)
#cap.set(10, 150)

# взять нужные элемент, определенный в файле main.py

color_ball = [0,15,117,255,110,255]  # красный
color_paddle = [106,113,255,255,90,120]  # синий
s = ""
s_prev = ""

def detectColor(img, colors1, colors2):
    x_ball = None
    y_ball = None
    x_paddle = None
    y_paddle = None
    global s
    global s_prev

    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower1 = np.array([colors1[0],colors1[2],colors1[4]])
    upper1 = np.array([colors1[1],colors1[3],colors1[5]])
    lower2 = np.array([colors2[0], colors2[2], colors2[4]])
    upper2 = np.array([colors2[1], colors2[3], colors2[5]])
    mask1 = cv2.inRange(hsv_img, lower1, upper1)
    mask2 = cv2.inRange(hsv_img, lower2, upper2)
    result1 = cv2.bitwise_and(img, img, mask=mask1)
    result2 = cv2.bitwise_and(img, img, mask=mask2)
    #cv2.imshow("result1", result1)
    #cv2.imshow("result2", result2)
    #cv2.imshow("result3", result3)
    moments1 = cv2.moments(mask1, 1)
    moments2 = cv2.moments(mask2, 1)
    x_m1 = moments1['m10']
    y_m1= moments1['m01']
    area1 = moments1['m00']
    x_m2 = moments2['m10']
    y_m2 = moments2['m01']
    area2 = moments2['m00']

    if area1 > 10:#указать нужное значение
        x_ball = int(x_m1/area1)
        y_ball = int(y_m1/area1)
        cv2.putText(img, str(x_ball)+","+str(y_ball), (x_ball,y_ball), \
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,255),2)
    if area2 > 10:  # указать нужное значение
        x_paddle = int(x_m2 / area2)
        y_paddle = int(y_m2 / area2)
        cv2.putText(img, str(x_paddle) + "," + str(y_paddle), (x_paddle, y_paddle), \
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

    if not(x_ball is None) and not(y_ball is None) and not(x_paddle is None) and not(y_paddle is None):
        s = ""
        if (x_ball < x_paddle - 20):
            s = "-1"
        elif (x_ball > x_paddle + 20):
            s = "1"
        else:
            s = "0"

        s = s + ","

        if (y_paddle - y_ball < 70):
            s = s + "1"
        else:
            s = s + "0"
        s += "\n"

        if s_prev != s:

            #if x_ball is None or y_ball is None:
            #    s = "0,0\n"
            print(s)
            arduinoSerial.write(s.encode())
            #print(arduinoSerial.read_all())

        s_prev = s
    else:
        print("err")
        s = "0,0\n"
        if s_prev != s:
            arduinoSerial.write(s.encode())
            print("stop")
        s_prev = s
    cv2.imshow("img", img)


while True:
    #if (arduinoSerial.inWaiting() > 0):
        #data = arduinoSerial.readline().decode().strip()
        #print(data)
    success, img = cap.read()
    img = cv2.flip(img, flipCode=0)
    #to_crop = cv2.flip(img, 1)
    #cropped = to_crop[0:350, 120:540]
    detectColor(img, color_ball, color_paddle)
    #cv2.imshow("result", img)
    cv2.waitKey(1)

cap.relise()
cv2.destroyAllWindows()