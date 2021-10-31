#!/usr/bin/python3
# Author: Shreyasta Samal
# -*- coding: utf-8 -*-
# @File : ExtractImagesFromVideos.py

import cv2

# Opens the Video file
cap= cv2.VideoCapture('resources/videos/A_16.avi')
i=0
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == False:
        break
    #cv2.imwrite('resources/images/'+ str(i) + '_.png',frame)
    cv2.imwrite('C:/Users/Shreyasta/PycharmProjects/Sarcomere/src/resources/images/sarcomere/A_16/original/'+ str(i) + '.png',frame)
    #cv2.imwrite('resources/images/'+ str(i) + '_gray.png',frame)
    i+=1

cap.release()
cv2.destroyAllWindows()