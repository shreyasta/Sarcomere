#!/usr/bin/python3
# Author: Shreyasta Samal
# -*- coding: utf-8 -*-
# @File : BrighnessContrast.py


from __future__ import print_function
from builtins import input
import cv2 as cv
import numpy as np
import argparse, os
# Read image given by user
# parser = argparse.ArgumentParser(description='Code for Changing the contrast and brightness of an image! tutorial.')
# parser.add_argument('--input', help='Path to input image.', default='lena.jpg')
# args = parser.parse_args()
#writing directory path
directory = 'C:/Users/Shreyasta/PycharmProjects/Sarcomere/src/resources/images/sarcomere/A_25/resize/'
# 
j=0
for i in os.listdir(directory):
    # print(type(i))
    # print(i)

    image = cv.imread('C:/Users/Shreyasta/PycharmProjects/Sarcomere/src/resources/images/sarcomere/A_25/resize/'+ i )
    print(image.shape)
    if image is None:
        print('Could not open or find the image: ')
        exit(0)
    new_image = np.zeros(image.shape, image.dtype)
    alpha = 3.5 # Simple contrast control
    beta = 10  # Simple brightness control
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
    #cv.imshow('Original Image', image)
    #cv.imshow('New Image', new_image)
    cv.imwrite('C:/Users/Shreyasta/PycharmProjects/Sarcomere/src/resources/images/sarcomere/A_25/resize_bright/'+ str(j) + '.tif', new_image)
    # Wait until user press some key
    j+=1
    cv.waitKey(0)
