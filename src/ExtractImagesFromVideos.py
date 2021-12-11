#!/usr/bin/python3
# Author: Shreyasta Samal
# -*- coding: utf-8 -*-
# @File : ExtractImagesFromVideos.py

import cv2

# Opens the Video file
cap= cv2.VideoCapture('resources/videos/A_25.AVI')
i=0
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == False:
        break
    print(i)
    #cv2.imwrite('resources/images/'+ str(i) + '_.png',frame)
    #cv2.imwrite('C:/Users/Shreyasta/PycharmProjects/Sarcomere/src/resources/images/sarcomere/A_25/original/'+ str(i) + '.png',frame)
    #cv2.imwrite('resources/images/'+ str(i) + '_gray.png',frame)
    i+=1

cap.release()
cv2.destroyAllWindows()

#note: In this file the values is printed in the right order. Only while retrieves and working on the image processing
#the problem arises.