#!/usr/bin/python3
# Author: Shreyasta Samal
# -*- coding: utf-8 -*-
# @File : Video2Gray.py


# importing the module
import cv2

# reading the video
source = cv2.VideoCapture('C:/Users/Shreyasta/PycharmProjects/Sarcomere/src/resources/videos/A_25.avi')
img_array = []
i = 0
# running the loop
while (source.isOpened()):

    # extracting the frames
    ret, img = source.read()
    if ret == False:
        break
    height, width, layer = img.shape
    size = (width, height)
    print('Size is: ')
    print(size)
    # converting to gray-scale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite('resources/images/sarcomere/A_25/gray/'+ str(i) + '_gray.png', gray )
    i+=1
    img_array.append(gray)
 #


        #print('Image array is: ')
        #print(img_array)

source.release()


#print(type(gray))
    # displaying the video
    #cv2.imshow("Live", gray)

    # exiting the loop
    #key = cv2.waitKey(1)
    #if key == ord("q"):
        #break





# closing the window
#cv2.destroyAllWindows()


# frameSize = (252, 252)
#
# img_array = []
# for filename in glob.glob('C:/Users/Shreyasta/PycharmProjects/Sarcomere/src/resources/images/sarcomere/A_2/contour/*.png'):
#     filename
#     img = cv2.imread(filename)
#     height, width, layers = img.shape
#     size = (width, height)
#     img_array.append(img)
#
# out = cv2.VideoWriter('C:/Users/Shreyasta/PycharmProjects/Sarcomere/src/resources/images/sarcomere/A_2/contour/sarcomere_A_2_contour.avi', cv2.VideoWriter_fourcc(*'DIVX'), 15, size)
#


