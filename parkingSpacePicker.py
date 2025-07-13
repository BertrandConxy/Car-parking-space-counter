import cv2
import pickle

img = cv2.imread("carParkImg.png")

width, height = 107, 48

try:
    with open('CarParkPos', 'rb') as f:
        posList = pickle.load(f)
except:
    posList = []


def mouseClick(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        posList.append((x, y))


    if event == cv2.EVENT_RBUTTONDOWN:
        for i, pos in enumerate(posList):
            if pos[0] < x < pos[0] + width and pos[1] < y < pos[1] + height:
                posList.pop(i)
                break
    with open('CarParkPos', 'wb') as f:
        pickle.dump(posList, f)


while True:
    img = cv2.imread("carParkImg.png")
    for pos in posList:
        cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), (255, 0, 255), 2)
    cv2.imshow("Image", img)
    cv2.setMouseCallback("Image", mouseClick)
    cv2.waitKey(1)