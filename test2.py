import cv2
import numpy as np

#img = cv2.imread('shapes.jpg', cv2.IMREAD_GRAYSCALE)
#img = cv2.imread('NSTAR_D20.jpg', cv2.IMREAD_GRAYSCALE)
#img = cv2.imread('testD202.jpg',  1)
img = cv2.imread('32g.jpg',  1)
#img = cv2.imread('d20v3.jpg',  1)
font = cv2.FONT_HERSHEY_SIMPLEX
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
dol = np.array([50, 50, 50])
gora = np.array([255, 255, 255])
maska = cv2.inRange(img_hsv, dol,gora)
obraz = cv2.bitwise_and(img, img, mask=maska)
#cv2.imshow('test',maska)
#print(img)
contours, _=cv2.findContours(maska, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

contour_list = []
for contour in contours:
    cv2.drawContours(obraz, contour, -1, (0, 255, 0), 3)
    approx = cv2.approxPolyDP(contour, 0.03*cv2.arcLength(contour, True), True)

    x = approx.ravel()[0]
    y = approx.ravel()[1]

    if 6 <= len(approx) < 7:
        cv2.putText(img, "D20", (x, y), font, 1, (0))

    else:
        cv2.putText(img, " ", (x, y), font, 1, (0))

    area = cv2.contourArea(contour)
    if ((len(approx) >5) & (area > 30)):
        contour_list.append(contour)


print('Liczba D20: {}'.format(int(len(contour_list)/2)))
cv2.imshow('image', img)
cv2.imshow('kolory', obraz)
cv2.imwrite('kolory.jpg',obraz)
#cv2.imshow("Threshhold", threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()