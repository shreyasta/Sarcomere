#!/usr/bin/python3
# Author: Shreyasta Samal
# -*- coding: utf-8 -*-
# @File : ConvexHullVideo.py


#!/usr/bin/python3
# Author: Shreyasta Samal
# -*- coding: utf-8 -*-
# @File : ConvexHull.py#

import cv2
import numpy as np
import glob, os, re

#make 2 videos a. outline b. points
my_path= "C:/Users/Shreyasta/PycharmProjects/Sarcomere/src/resources/images/sarcomere/A_25/cropped/*.png"
directory = glob.glob(my_path)

img_array = []
x=[]
for i in directory:
   print(i)
   j = int(re.split('[\W]', i)[-2])
   print('j is ', j)
   img = cv2.imread(i)
   height, width, layers = img.shape
   size = (width, height)
   g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
   edge = cv2.Canny(g, 130, 180)
   contours, hierarchy = cv2.findContours(edge, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
   for c in contours:
       #print('c is ', c)
       hull = cv2.convexHull(c)
       #print('hull is ', hull)
       # outline
       #cv2.drawContours(img, [hull], 0, (0, 0, 255), 0)
       #points
       cv2.drawContours(img, hull, 0, (0, 0, 255), 2)
       #
       cv2.imwrite('C:/Users/Shreyasta/PycharmProjects/Sarcomere/src/resources/images/sarcomere/A_25/convex_hull/cropped_points/' + str(j) + '.png', img)
       # Wait until user press some key

#Save the images correctly and then later look into the video making part of it.


   #cv2.imshow(i, img)
   #cv2.waitKey(0)
   #img = cv2.resize(img, (frameWidth, frameHeight))

#
# # trying to save the code in a video format
# out = cv2.VideoWriter('C:/Users/Shreyasta/PycharmProjects/Sarcomere/src/resources/videos/A_25_convex_points.avi', cv2.VideoWriter_fourcc(*'DIVX'), 15, size)
#
# for i in range(len(img_array)):
#    out.write(img_array[i])
# out.release()