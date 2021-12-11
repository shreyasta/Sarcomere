#!/usr/bin/python3
# Author: Shreyasta Samal
# -*- coding: utf-8 -*-
# @File : LK_OpticalFlow.py
import cv2
import numpy as np



# Read the video
#cap = cv2.VideoCapture(video_path)

cap = cv2.imread('C:/Users/Shreyasta/PycharmProjects/Sarcomere/src/resources/Cropped Image.png')
# Parameters for ShiTomasi corner detection
feature_params = dict(maxCorners=100, qualityLevel=0.3, minDistance=7, blockSize=7)

# Parameters for Lucas Kanade optical flow
lk_params = dict(
    winSize=(15, 15),
    maxLevel=2,
    criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03),
)

# Create random colors
color = (0, 0, 255)

# Take first frame and find corners in it
#ret, old_frame = cap.read()
old_frame = cap
old_gray = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)
p0 = cv2.goodFeaturesToTrack(old_gray, mask=None, **feature_params)
print(p0)
# Create a mask image for drawing purposes
mask = np.zeros_like(old_frame)

while True:
    # Read new frame
    frame = cap
    #ret, frame = cap.read()
    # if not ret:
    #     break
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Calculate Optical Flow
    p1, st, err = cv2.calcOpticalFlowPyrLK(
        old_gray, frame_gray, p0, None, **lk_params
    )
    # Select good points
    good_new = p1[st == 1]
    good_old = p0[st == 1]

    # Draw the tracks
    for i, (new, old) in enumerate(zip(good_new, good_old)):
        a, b = new.ravel()
        c, d = old.ravel()
        mask = cv2.line(mask, (a, b), (c, d), color, 2)
        frame = cv2.circle(frame, (a, b), 2, color, -1)

    # Display the demo
    img = cv2.add(frame, mask)
    cv2.imshow("frame", img)
    #cv2.waitKey(1)
    k = cv2.waitKey(25) & 0xFF
    if k == 27:
        break

    # Update the previous frame and previous points
    old_gray = frame_gray.copy()
    p0 = good_new.reshape(-1, 1, 2)