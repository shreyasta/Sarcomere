#!/usr/bin/python3
# Author: Shreyasta Samal
# -*- coding: utf-8 -*-
# @File : Image2VideosTest.py

import cv2
import numpy as np
import glob

img_array = []
for filename in glob.glob('C:/Users/Shreyasta/PycharmProjects/Sarcomere/src/resources/images/sarcomere/A_25/cropped/*.png'):
   img = cv2.imread(filename)
   height, width, layers = img.shape
   size = (width, height)
   print(size)
   img_array.append(img)

print(len(img_array))



out = cv2.VideoWriter('C:/Users/Shreyasta/PycharmProjects/Sarcomere/src/resources/videos/A_25_cropped_test1.avi', cv2.VideoWriter_fourcc(*'DIVX'), 15, (188,312))

for i in range(len(img_array)):
   out.write(img_array[i])
out.release()