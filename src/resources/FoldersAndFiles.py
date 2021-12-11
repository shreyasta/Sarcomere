#!/usr/bin/python3
# Author: Shreyasta Samal
# -*- coding: utf-8 -*-
# @File : FoldersAndFiles.py

import os, re
import cv2
import glob
my_path='images/sarcomere/A_2/original/'
new_path = 'C:/Users/Shreyasta/PycharmProjects/Sarcomere/src/resources/images/sarcomere/A_25/trial/'
files=glob.glob(my_path+'*.png')
# the files are not printed numerically


dirFiles=[]
print(len(files))
for i in files:
    dirFiles.append(i)
    #print(i)



#sorted(dirFiles, key = lambda x: int(re.split('[/W]',x)[-2]))
#print(dirFiles)
x=[]
for i in dirFiles:
    x.append(int(re.split('[\W]', i)[-2]))

#print(x)

#That's hpw I get sorted numbers
#print(sorted(x))
y = sorted(x)

for j in y:
    print(j)
    print(new_path+ str(j) + '.png')
    #print(type(j))