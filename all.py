import numpy as np
import cv2
import os

path = './1/'
x = [item for item in os.listdir(path)]
print(x)

for i in range(len(x)):
    image = cv2.imread(path+x[i])
    blur = cv2.GaussianBlur(image, (7,7), 0)
    hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)
    lower = np.array([94, 80, 2])
    upper = np.array([126, 255, 255])
    mask = cv2.inRange(hsv, lower, upper)
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=1)
    close = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel, iterations=3)
    cv2.imwrite(x[i]+'-blue_Epi.png',close)

'''
for i in range(len(x)):
    image = cv2.imread(path+x[i])
    blur = cv2.GaussianBlur(image, (7,7), 0)
    hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)
    lower = np.array([25, 52, 72])
    upper = np.array([102, 255, 255])
    mask = cv2.inRange(hsv, lower, upper)
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=1)
    close = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel, iterations=3)
    cv2.imwrite(x[i]+'_green.png',close)

'''

for i in range(len(x)):
    image = cv2.imread(path+x[i])
    blur = cv2.GaussianBlur(image, (7,7), 0)
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower = np.array([161, 155, 84])
    upper = np.array([179, 255, 255])
    mask = cv2.inRange(hsv, lower, upper)
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=1)
    close = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel, iterations=3)
    cv2.imwrite(x[i]+'-red_nuc.png',close)


for i in range(len(x)):
    image = cv2.imread(path+x[i])
    blur = cv2.GaussianBlur(image, (7,7), 0)
    hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)
    lower = np.array([22, 93, 0])
    upper = np.array([45, 255, 255])
    mask = cv2.inRange(hsv, lower, upper)
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=1)
    close = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel, iterations=3)
    cv2.imwrite(x[i]+'_yellow-immune.png',close)
