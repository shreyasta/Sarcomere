#!/usr/bin/python3
# Author: Shreyasta Samal
# -*- coding: utf-8 -*-
# @File : ConvertImages2VideosTest.py


import cv2
import numpy as np
import glob

# resizing the frameWidth and frameHeight
frameWidth = 252
frameHeight = 252

img_array = []
for filename in glob.glob('C:/Users/Shreyasta/PycharmProjects/Sarcomere/src/resources/images/sarcomere/A_25/resize_bright/*.tif'):
   print(filename)
   img = cv2.imread(filename)
   height, width, layers = img.shape

   size = (width, height)
   #img = cv2.resize(img, (frameWidth, frameHeight))
   print(size)
   print(len(img_array))

# img_array, size = resize(img_array, 'largest')
# out = cv2.VideoWriter('C:/Users/Shreyasta/PycharmProjects/Sarcomere/src/resources/videos/A_25_bright_resize_testsize.avi', cv2.VideoWriter_fourcc(*'DIVX'), 15, size)
#
# for i in range(len(img_array)):
#     #print(i)
#     out.write(img_array[i])
#out.release()