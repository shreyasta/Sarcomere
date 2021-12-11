#!/usr/bin/python3
# Author: Shreyasta Samal
# -*- coding: utf-8 -*-
# @File : Contour.py

import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('C:/Users/Shreyasta/PycharmProjects/Sarcomere/src/resources/images/sarcomere/A_25/resize_bright/1.tif')
# image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
# fig, ax = plt.subplots(1, figsize=(12,8))
# plt.imshow(image)
# cv2.imshow('New', image)
# cv2.waitKey(0)

g = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
edge = cv2.Canny(g, 130, 150)
fig, ax = plt.subplots(1, figsize=(12,8))
contours = cv2.findContours(edge,
                            cv2.RETR_EXTERNAL,
                            cv2.CHAIN_APPROX_NONE)
cv2.drawContours(image, contours[0], -1, (0,0,255), thickness = 0)


#plt.imshow(edge, cmap='Greys')
cv2.imshow('New', image)
cv2.waitKey(0)