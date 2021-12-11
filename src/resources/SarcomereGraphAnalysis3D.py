#!/usr/bin/python3
# Author: Shreyasta Samal
# -*- coding: utf-8 -*-
# @File : SarcomereGraphAnalysis3D.py
import numpy as np
from numpy import genfromtxt
import matplotlib.pyplot as plt

sarc_data = genfromtxt('C:/Users/Shreyasta/PycharmProjects/Sarcomere/src/sub_df_3.csv', delimiter=',', skip_header = 1)
sarc_data_2 = genfromtxt('C:/Users/Shreyasta/PycharmProjects/Sarcomere/src/sub_df_2.csv', delimiter=',', skip_header = 1)
#print(sarc_data)


# delete 1 st column and 3 rd
# column at a time
data = np.delete(sarc_data, [0, 1, 4,5], 1)
data_2 = np.delete(sarc_data_2, [0, 1, 4,5], 1)
#print("data  after 1 st and 3 rd column  deleted :\n", data)
#print(type(data))
# x,y coordinates of data
x, y = data[:, 0], data[:, 1]
x_2, y_2 = data_2[:, 0], data_2[:, 1]

count = np.count_nonzero(x)
print(count)

#fig = plt.figure()
#ax = fig.add_subplot(111, projection = '3d')
x_cr = x
y_cr = y

# Creating figure
fig = plt.figure(figsize=(10, 7))
#ax = plt.axes(projection="3d")

#Creating plot
#ax.scatter3D(x_cr, y_cr, color="red")
#plt.title("simple 3D scatter plot")
#ax = data.plot(kind='scatter', x='x_cr', y='y_cr', color='DarkBlue', label='Group 1')
#data_2.plot(kind='scatter', x='x_2', y='y_2', color='DarkGreen', label='Group 2', ax=ax)


#show plot

plt.plot(x_cr, y_cr, label="Sarc point 1", linestyle="-")
plt.plot(x_2, y_2, label="Sarc point 2", linestyle="--")
plt.xlabel("X coordinate")
plt.ylabel("Y coordinate")
plt.legend()
plt.show()




