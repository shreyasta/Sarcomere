#!/usr/bin/python3
# Author: Shreyasta Samal
# -*- coding: utf-8 -*-
# @File : Lucas-KanadeOpticalFlow.py


import numpy as np
import cv2 as cv
import csv
import pandas as pd
import argparse
# parser = argparse.ArgumentParser(description='This sample demonstrates Lucas-Kanade Optical Flow calculation. /
#                                               The example file can be downloaded from: /
#                                               https://www.bogotobogo.com/python/OpenCV_Python/images/mean_shift_tracking/slow_traffic_small.mp4')
# parser.add_argument('image', type=str, help='path to image file')
# args = parser.parse_args()
cap = cv.VideoCapture('C:/Users/Shreyasta/PycharmProjects/Sarcomere/src/resources/videos/A_24.avi')
# params for ShiTomasi corner detection
feature_params = dict( maxCorners = 75,
                       qualityLevel = 0.3,
                       minDistance = 7,
                       blockSize = 7 )
# Parameters for lucas kanade optical flow
lk_params = dict( winSize  = (8,8),
                  maxLevel = 2,
                  criteria = (cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 0.03))
# Create some random colors
#color = np.random.randint(0,255,(100,3))
# Fixing the colour
color = (0, 0, 255)
# Take first frame and find corners in it
ret, old_frame = cap.read()
old_gray = cv.cvtColor(old_frame, cv.COLOR_BGR2GRAY)
p0 = cv.goodFeaturesToTrack(old_gray, mask = None, **feature_params)
print(type(p0))
print(len(p0))
# for i in p0:
#     print(f"Points at p0  are {i} " )
# Create a mask image for drawing purposes
mask = np.zeros_like(old_frame)
while(1):
    ret,frame = cap.read()
    frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # calculate optical flow
    p1, st, err = cv.calcOpticalFlowPyrLK(old_gray, frame_gray, p0, None, **lk_params)
    # Select good points
    if p1 is not None:
        good_new = p1[st==1]
        good_old = p0[st==1]
    # draw the tracks

    # with open('A_24.csv', 'w', newline='') as csvfile:
    #     fieldnames = ['frame_num', 'a', 'b', 'c', 'd']
    #     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    #     writer.writeheader()


    for i,(new,old) in enumerate(zip(good_new, good_old)):
        a,b = new.ravel()
        c,d = old.ravel()
        #mask = cv.line(mask, (int(a),int(b)),(int(c),int(d)), color[i].tolist(), 2)
        # Making all the colours to red
        # Mask provides the distance traveled
        mask = cv.line(mask, (int(a),int(b)),(int(c),int(d)), color, 2)
        #print(f"Coordinates of the high intesity points from line are {i} are {a} {b} and {c} {d}")
        # Frame gives us only the coordinates of the high intensity points on the sarcomere
        #frame = cv.circle(frame,(int(a),int(b)),2,color[i].tolist(),-1)
        frame = cv.circle(frame,(int(a),int(b)),2,color,-1)
        # print on the console
        #with open()
        print(f" {i} ,{a}, {b}" )
        # printing on the excel file
        #rows.append([i, a, b])
        #print(rows)

            #writer.writerow({'frame_num': f"{i}", 'a': f"{a}", 'b': f"{b}", 'c': f"{c}", 'd': f"{d}"})


# print
# m += 1
# print('image is %d, %d', i, m)
# img2 = cvCoordinates.add(frame, mask)
# cv.imwrite('C:/Users/Shreyasta/PycharmProjects/Sarcomere/src/resources/lucas_kanade/' + str(i) + '_lk_.png',
#            img2)
        img = cv.add(frame,mask)




        cv.imshow('frame',img)


        k = cv.waitKey(100) & 0xff
        if k == 27:
            break
        # Now update the previous frame and previous points
        old_gray = frame_gray.copy()
        p0 = good_new.reshape(-1,1,2)

    # df = pd.DataFrame(rows, columns=["A", "B"])
    # print(df)
