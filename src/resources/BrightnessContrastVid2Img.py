#!/usr/bin/python3
# Author: Shreyasta Samal
# -*- coding: utf-8 -*-
# @File : BrightnessContrastVid2Img.py

#!/usr/bin/python3
# Author: Shreyasta Samal
# -*- coding: utf-8 -*-
# @File : BrighnessContrast.py


from __future__ import print_function
from builtins import input
import cv2 as cv
import numpy as np
import argparse
# Read image given by user
# parser = argparse.ArgumentParser(description='Code for Changing the contrast and brightness of an image! tutorial.')
# parser.add_argument('--input', help='Path to input image.', default='lena.jpg')
# args = parser.parse_args()

image = cv.imread('C:/Users/Shreyasta/PycharmProjects/Sarcomere/src/resources/images/sarcomere/A_25/original/1.png')
print(image.shape)
if image is None:
    print('Could not open or find the image: ')
    exit(0)
new_image = np.zeros(image.shape, image.dtype)
alpha = 2.0 # Simple contrast control
beta = 60  # Simple brightness control
# Initialize values
print(' Basic Linear Transforms ')
print('-------------------------')
# try:
#     alpha = float(input('* Enter the alpha value [1.0-3.0]: '))
#     beta = int(input('* Enter the beta value [0-100]: '))
# except ValueError:
#     print('Error, not a number')
# Do the operation new_image(i,j) = alpha*image(i,j) + beta
# Instead of these 'for' loops we could have used simply:
new_image = cv.convertScaleAbs(image, alpha=alpha, beta=beta)
# but we wanted to show you how to access the pixels :)
# print('The image analysis')
# for y in range(image.shape[0]):
#     for x in range(image.shape[1]):
#         for c in range(image.shape[2]):
#             new_image[y,x,c] = np.clip(alpha*image[y,x,c] + beta, 0, 255)
cv.imshow('Original Image', image)
cv.imshow('New Image', new_image)
cv.imwrite('C:/Users/Shreyasta/PycharmProjects/Sarcomere/src/resources/images/sarcomere/A_25/bright/1.png',new_image)
# Wait until user press some key
cv.waitKey(0)








# Opens the Video file
cap= cv2.VideoCapture('resources/videos/A_25.avi')
i=0
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == False:
        break
    if frame is None:
        print('Could not open or find the image: ')
        exit(0)
    new_image = np.zeros(frame.shape, frame.dtype)
    alpha = 2.0  # Simple contrast control
    beta = 60  # Simple brightness control
    # Initialize values
    print(' Basic Linear Transforms ')
    print('-------------------------')
    # try:
    #     alpha = float(input('* Enter the alpha value [1.0-3.0]: '))
    #     beta = int(input('* Enter the beta value [0-100]: '))
    # except ValueError:
    #     print('Error, not a number')
    # Do the operation new_image(i,j) = alpha*image(i,j) + beta
    # Instead of these 'for' loops we could have used simply:
    new_image = cv2.convertScaleAbs(frame, alpha=alpha, beta=beta)
    # but we wanted to show you how to access the pixels :)
    # print('The image analysis')
    # for y in range(image.shape[0]):
    #     for x in range(image.shape[1]):
    #         for c in range(image.shape[2]):
    #             new_image[y,x,c] = np.clip(alpha*image[y,x,c] + beta, 0, 255)
    cv2.imshow('Original Image', frame)
    cv2.imshow('New Image', new_image)
    cv2.imwrite('C:/Users/Shreyasta/PycharmProjects/Sarcomere/src/resources/images/sarcomere/A_25/bright/'+ str(i) + '.png',
               new_image)
    i += 1
    # Wait until user press some key
    #cv2.waitKey(0)


cap.release()
cv2.destroyAllWindows()

