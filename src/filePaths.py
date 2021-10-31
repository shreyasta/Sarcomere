#!/usr/bin/python3
# Author: Shreyasta Samal
# -*- coding: utf-8 -*-
# @File : filePaths.py


import os,glob
#print(os.listdir('/path/to/folder/to/list'))

def sort(lst):
    lst = [str(i) for i in lst]
    lst.sort()
    lst = [int(i) if i.isdigit() else i for i in lst]
    return lst
#
#
# # Driver code
# lst = ['k', 5, 'e', 3, 'g', 7, 0, 't']



myimages = []  # list of image filenames
dirFiles = os.listdir('C:/Users/Shreyasta/PycharmProjects/Sarcomere/src/resources/images/sarcomere/A_2')  # list of directory files
#print(dirFiles)

my_path='C:/Users/Shreyasta/PycharmProjects/Sarcomere/src/resources/images/sarcomere/A_2/'
my_path_save = 'C:/Users/Shreyasta/PycharmProjects/Sarcomere/src/resources/images/sarcomere/A_2/contour/'
files=glob.glob(my_path+'*.png')


for j in files:
    print(j.rsplit('_', 1)[1])
    x=j.rsplit('_', 1)[1]
    print(sort(x))
    # cv.imwrite(my_path + str(j) + '_contour.png', drawing)
    # print(my_path + 'sarcomere_A_2_' + str(x) + '_contour.png')
    #cv.imwrite('contour_' + j.rsplit('.', 1)[0] + '.png', drawing)



# Python3 program to Sort list
# containing alpha and numeric values
# Python3 program to Sort list
# containing alpha and numeric values

# def sort(lst):
#     return sorted(lst, key=str)
#
#
# # Driver code
# lst = ['k', 5, 'e', 3, 'g', 7, 0, 't']
# print(sort(lst))


# def sort(lst):
#     return sorted(lst, key=lambda x: (isinstance(x, str), x))
#
#
# # Driver code
# lst = ['k', 5, 'e', 3, 'g', 7, 0, 't']
# print(sort(dirFiles))
# Python3 program to Sort list
# containing alpha and numeric values




