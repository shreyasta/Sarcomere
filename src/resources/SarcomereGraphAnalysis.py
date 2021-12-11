#!/usr/bin/python3
# Author: Shreyasta Samal
# -*- coding: utf-8 -*-
# @File : SarcomereGraphAnalysis.py


import numpy as np
from numpy import genfromtxt
import matplotlib.pyplot as plt

sarc_data = genfromtxt('C:/Users/Shreyasta/PycharmProjects/Sarcomere/src/sub_df_1.csv', delimiter=',', skip_header = 1)
#print(sarc_data)


# delete 1 st column and 3 rd
# column at a time
data = np.delete(sarc_data, [0, 1, 4,5], 1)
#print("data  after 1 st and 3 rd column  deleted :\n", data)
#print(type(data))
# x,y coordinates of data
x, y = data[:, 0], data[:, 1]

print(x)

# plotting
plt.title("Line graph")
plt.xlabel("X axis")
plt.ylabel("Y axis")
#plt.plot(x, y, color ="red")
plt.scatter(x, y)
plt.show()