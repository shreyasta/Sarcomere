#!/usr/bin/python3
# Author: Shreyasta Samal
# -*- coding: utf-8 -*-
# @File : SarcPointsMinMaxCalculation.py
import numpy as np
from numpy import genfromtxt
import matplotlib.pyplot as plt

sarc_data = genfromtxt('C:/Users/Shreyasta/PycharmProjects/Sarcomere/src/sub_df_18.csv', delimiter=',', skip_header = 1)
sarc_data_2 = genfromtxt('C:/Users/Shreyasta/PycharmProjects/Sarcomere/src/sub_df_27.csv', delimiter=',', skip_header = 1)
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

# picking the min and max of all the x-coordinates and the index, then find the corresponding y coord
print('Point 27')
print(min(x_2))
print(max(x_2))

print('Maximum Value',data[52])
print('Minimum Value',data[236])
print('Max Value')
# Point 18 min and max values
point18_min = data[236]
point18_max = data[52]

# Point 27 min and max values
point27_min = data_2[0]
point27_max = data_2[143]

# calculating Euclidean distance
# using linalg.norm()
Min_Max_Dist_Point_18 = np.linalg.norm(point18_min - point18_max)

# printing Euclidean distance
print('Distance between minimum and maximum of point 18  is ', Min_Max_Dist_Point_18)
#print('y_2')
#print(y_2)

# Distance between Minimum point between point 18 and 27

Min_Point18_Point27 = np.linalg.norm(point18_min - point27_min)

# printing Euclidean distance
print('Distance between minimum of points 18 and 27  is ', Min_Point18_Point27)



# Distance between Maximum point between point 18 and 27

Max_Point18_Point27 = np.linalg.norm(point18_max - point27_max)

# printing Euclidean distance
print('Distance between maximum of points 18 and 27  is ', Max_Point18_Point27)


# result_max_index = np.where(x_2 == np.amax(x_2))
# result_min_index = np.where(x == np.amin(x))
# print(result_max_index)
# print(result_min_index)
# count = np.count_nonzero(x)
# print(count)

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

#plt.plot(x_cr, y_cr, label="Sarc point 1", linestyle="_")
plt.scatter(x_cr, y_cr, color= 'red', label="Sarc point 18")
#plt.plot(x_2, y_2, label="Sarc point 2", linestyle="--")
plt.scatter(x_2, y_2, label="Sarc point 27", linestyle="--")
plt.xlabel("X coordinate")
plt.ylabel("Y coordinate")
plt.legend()
plt.show()




