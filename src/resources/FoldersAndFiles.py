#!/usr/bin/python3
# Author: Shreyasta Samal
# -*- coding: utf-8 -*-
# @File : FoldersAndFiles.py

import os
import glob
my_path='images/sarcomere/A_2/original/'
files=glob.glob(my_path+'*.png')

print(len(files))
for i in files:
    print(i)


