#!/usr/bin/python3
# Author: Shreyasta Samal
# -*- coding: utf-8 -*-
# @File : ConvexHull.py#

import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('C:/Users/Shreyasta/PycharmProjects/Sarcomere/src/resources/images/sarcomere/A_25/cropped/1.png')
#image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
g = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
edge = cv2.Canny(g, 130, 180)
contours, hierarchy = cv2.findContours(edge, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
for c in contours:
    hull = cv2.convexHull(c)
    print(hull)
    #cv2.drawContours(image, [hull], 0, (0, 0, 255), 0)
    cv2.drawContours(image, hull, 0, (0, 0, 255), 2)
fig, ax = plt.subplots(1, figsize=(12,8))
cv2.imshow('New', image)
cv2.waitKey(0)
#plt.imshow(image)