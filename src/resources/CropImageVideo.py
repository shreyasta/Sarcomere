#!/usr/bin/python3
# Author: Shreyasta Samal
# -*- coding: utf-8 -*-
# @File : CropImageVideo.py

import cv2, glob, os, re
import numpy as np


save_dir= 'C:/Users/Shreyasta/PycharmProjects/Sarcomere/src/resources/images/sarcomere/A_25/cropped/'
img_array = []
for filename in glob.glob('C:/Users/Shreyasta/PycharmProjects/Sarcomere/src/resources/images/sarcomere/A_25/resize_bright_better/*.png'):
   j =int(re.split('[\W]', filename)[-2])
   print(j)
   img = cv2.imread(filename)
   #print(img.shape) # Print image shape
   # Cropping an image
   #cropped = img[start_row:end_row, start_col:end_col]
   cropped_image = img[40:352, 230:418]
   cv2.imwrite(save_dir + str(j) +'.png', cropped_image)


# Display cropped image


# Save the cropped image


cv2.waitKey(0)
cv2.destroyAllWindows()