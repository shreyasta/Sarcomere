#!/usr/bin/python3
# Author: Shreyasta Samal
# -*- coding: utf-8 -*-
# @File : Read_Video.py
import cv2

#
# frameWidth = 640
# frameHeight = 480
#cap = cv2.VideoCapture("blink_detection_demo.mp4")
# cap = cv2.VideoCapture("resources/videos/A_25.avi")
# while True:
#     success, img = cap.read()
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     img = cv2.resize(gray, (frameWidth, frameHeight))
#     print(img.shape)
#     cv2.imshow("Result", gray)
#     if cv2.waitKey(100) and 0xFF == ord('q'):
#         break


import cv2

frameWidth = 640
frameHeight = 480
# cap = cv2.VideoCapture("blink_detection_demo.mp4")
cap = cv2.VideoCapture("resources/videos/A_25.avi")
i = 0
while True:
    success, img = cap.read()
    img = cv2.resize(img, (frameWidth, frameHeight))
    cv2.imwrite('C:/Users/Shreyasta/PycharmProjects/Sarcomere/src/resources/images/sarcomere/A_25/resize/'+ str(i) + '.png', img)
    cv2.imshow("Result", img)
    print(i)
    i+=1
    if cv2.waitKey(1) and 0xFF == ord('q'):
        break





# cap = cv2.VideoCapture("C:/Users/Shreyasta/PycharmProjects/Sarcomere/src/resources/videos/A_1.avi")
# while True:
#     success, img = cap.read()
#     #img = cv2.resize(img, (frameWidth, frameHeight))
#     cv2.imshow("Result", img)
#     if cv2.waitKey(1) and 0xFF == ord('q'):
#         break


