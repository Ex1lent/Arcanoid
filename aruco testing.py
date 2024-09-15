import cv2
import numpy as np
import os

# cap = cv2.VideoCapture(1)
img = cv2.imread('pics/test1.jpg')
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

x = (final_array[0][0]+final_array[2][0])//2
y = (final_array[0][1]+final_array[2][1])//2
cv2.putText(img, str(ids[0][0]), [x, y], 2, 1, (0, 255, 0), 1, cv2.LINE_AA)
img = cv2.circle(img, (x,y), radius=2, color=(255, 0, 0), thickness=3)
cv2.imshow('1', img)
cv2.waitKey(0);
cv2.destroyAllWindows()
print(x,y)

def detectColors():
    pass
