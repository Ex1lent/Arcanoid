import cv2
import numpy as np

aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_250)

marker_id = 13
marker_size = 200
marker_img = cv2.aruco.generateImageMarker(aruco_dict, marker_id, marker_size)
cv2.imwrite('pics/marker_13.png', marker_img)
