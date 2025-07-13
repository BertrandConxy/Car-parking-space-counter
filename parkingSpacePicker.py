import cv2
import pickle

img = cv2.imread("carParkImg.png")

while True:
    cv2.rectangle(img, (50, 192), (157, 240), (255, 0, 255), 2)
    cv2.imshow("Image", img)
    cv2.waitKey(1)