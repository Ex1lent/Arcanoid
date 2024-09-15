import cv2

cap = cv2.VideoCapture(0)
success, img = cap.read()
img = cv2.flip(img, 1)

# [rows, columns]
crop = img[0:350, 120:540]

cv2.imshow('original', img)
cv2.imshow('cropped', crop)
cv2.waitKey(0)
cv2.destroyAllWindows()