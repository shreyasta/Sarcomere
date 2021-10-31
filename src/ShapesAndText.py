#!/usr/bin/python3
# Author: Shreyasta Samal
# -*- coding: utf-8 -*-
# @File : ShapesAndText.py

import cv2
import numpy as np

#img = np.zeros((512, 512, 3), np.uint8)
img = cv2.imread('C:/Users/Shreyasta/PycharmProjects/Sarcomere/src/resources/images/sarcomere_A_2_5.png')
print(img.shape)
# img&amp;#91;:]= 255,0,0
imgCanny = cv2.Canny(img, 150, 200)
color = (0, 255, 255)
cv2.line(img, (0, 0), (10, 56), color)
cv2.rectangle(img, (0, 0), (250, 350),(0, 0, 255),2)
cv2.circle(img, (125, 50), 3, color, 0)
cv2.putText(img, " OPENCV  ", (300, 200), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 150, 0), 3)

cv2.imshow("Image", img)
cv2.imshow("Canny Image", imgCanny)
cv2.waitKey(0)