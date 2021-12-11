#!/usr/bin/python3
# Author: Shreyasta Samal
# -*- coding: utf-8 -*-
# @File : Crop_image.py


# Import packages
import cv2
import numpy as np

img = cv2.imread('C:/Users/Shreyasta/PycharmProjects/Sarcomere/src/resources/images/sarcomere/A_25/resize_bright_better/0.png')
print(img.shape) # Print image shape
cv2.imshow("original", img)

# Cropping an image
#cropped = img[start_row:end_row, start_col:end_col]
cropped_image = img[40:352, 230:418]

# Display cropped image
cv2.imshow("cropped", cropped_image)

# Save the cropped image
cv2.imwrite("Cropped Image.png", cropped_image)

cv2.waitKey(0)
cv2.destroyAllWindows()