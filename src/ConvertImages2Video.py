#!/usr/bin/python3
# Author: Shreyasta Samal
# -*- coding: utf-8 -*-
# @File : ConvertImages2Video.py

import cv2
import numpy as np
import glob, os

#frameSize = (252, 252)

# img_array = []
# for filename in glob.glob('C:/Users/Shreyasta/PycharmProjects/Sarcomere/src/resources/images/sarcomere/A_2/contour/*.png'):
#     filename
#     img = cv2.imread(filename)
#     height, width, layers = img.shape
#     size = (width, height)
#     img_array.append(img)
#
# out = cv2.VideoWriter('C:/Users/Shreyasta/PycharmProjects/Sarcomere/src/resources/images/sarcomere/A_2/contour/sarcomere_A_2_contour.avi', cv2.VideoWriter_fourcc(*'DIVX'), 15, size)

#import glob
#print(glob.glob('C:/Users/Shreyasta/PycharmProjects/Sarcomere/src/resources/images/sarcomere/A_2/contour/*'))




# myimages = []  # list of image filenames
# dirFiles = os.listdir('C:/Users/Shreyasta/PycharmProjects/Sarcomere/src/resources/images')  # list of directory files
# x= dirFiles.sort()  # good initial sort but doesnt sort numerically very well
#sorted(dirFiles)  # sort numerically in ascending order

# for files in dirFiles: #filter out all non jpgs
#    if '.png' in files:
#        print(files)
#         myimages.append(files)
# print(len(myimages))
# print(myimages)

# os.chdir("C:/Users/Shreyasta/PycharmProjects/Sarcomere/src/resources/images/sarcomere/A_2/contour/")
# for file in glob.glob("*.png"):
#     print(file)
#
# import os
#
# os.chdir("C:/Users/Shreyasta/PycharmProjects/Sarcomere/src/resources/images")
# for root, dirs, files in os.walk(".", topdown = True):
#    #for name in files:
#       #print(os.path.join(root, name))
#    for name in dirs:
#        print(os.path.join(root, name))

# import glob
#
# # Recursively print png imageC:/Users/Shreyasta/PycharmProjects/Sarcomere/src/resources/lucas_kanades in folder C:/Users/admin/
# for filepath in glob.iglob(r'C:/Users/Shreyasta/PycharmProjects/Sarcomere/src/resources/images/*.png', recursive=False):
#    print(filepath)

import cv2
import numpy as np
import glob

img_array = []
for filename in glob.glob('C:/Users/Shreyasta/PycharmProjects/Sarcomere/src/resources/lucas_kanade/*.png'):
   img = cv2.imread(filename)
   height, width, layers = img.shape
   size = (width, height)
   print(size)
   img_array.append(img)

print(len(img_array))



out = cv2.VideoWriter('C:/Users/Shreyasta/PycharmProjects/Sarcomere/src/resources/lucas_kanade/A_2_lk.avi', cv2.VideoWriter_fourcc(*'DIVX'), 15, size)

for i in range(len(img_array)):
   out.write(img_array[i])
out.release()