import cv2
import numpy as np
# import serial
import time

# arduinoSerial = serial.Serial('COM8', 9600)
time.sleep(2)
# cap = cv2.VideoCapture(1)
color_ball = [0, 9, 200, 255, 200, 255]
s = ""
s_prev = ""


def detectcolors(img, colors1):
    # color part ||||||||||||||||||||||||||||||||||||||
    x_ball, y_ball = None, None
    x_paddle, y_paddle = None, None
    global s, s_prev
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower1 = np.array([colors1[0], colors1[2], colors1[4]])
    upper1 = np.array([colors1[1], colors1[3], colors1[5]])
    mask1 = cv2.inRange(hsv_img, lower1, upper1)
    result1 = cv2.bitwise_and(img, img, mask=mask1)
    moments1 = cv2.moments(mask1, 1)
    x_m1 = moments1['m10']
    y_m1 = moments1['m01']
    area1 = moments1['m00']

    if area1 > 10:
        x_ball = int(x_m1 / area1)
        y_ball = int(y_m1 / area1)
        cv2.putText(img, str(x_ball) + "," + str(y_ball), (x_ball, y_ball), \
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
    # arUco part |||||||||||||||||||||||||||||||||||||||
    img = cv2.circle(img, (x_ball, y_ball), radius=2, color=(255, 0, 0), thickness=3)
    imgAruco = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_250)
    parameters = cv2.aruco.DetectorParameters()
    det = cv2.aruco.ArucoDetector(dictionary, parameters)
    corners, ids, _ = det.detectMarkers(imgAruco)

    # переформирование массива
    final_array = np.array(corners[0][0], dtype='int16')

    # обводка метки
    cv2.line(img, final_array[0], final_array[1], (0, 255, 0), thickness=2)
    cv2.line(img, final_array[1], final_array[2], (0, 255, 0), thickness=2)
    cv2.line(img, final_array[2], final_array[3], (0, 255, 0), thickness=2)
    cv2.line(img, final_array[3], final_array[0], (0, 255, 0), thickness=2)

    # рассчет координат
    x = (final_array[0][0] + final_array[2][0]) // 2
    y = (final_array[0][1] + final_array[2][1]) // 2
    cv2.putText(img, str(ids[0][0]), [x, y], 2, 1, (0, 255, 0), 1, cv2.LINE_AA)
    img = cv2.circle(img, (x, y), radius=2, color=(255, 0, 0), thickness=3)
    cv2.line(img, [x_ball, y_ball], [x_ball, y], (255, 100, 0), thickness=2)
    cv2.line(img, [x, y], [x_ball, y], (255, 100, 0), thickness=2)

    # показ картинки
    cv2.imshow("Testing...", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


image = cv2.imread('pics/test1.jpg')
detectcolors(image, color_ball)
