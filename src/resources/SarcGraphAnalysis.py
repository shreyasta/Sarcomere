#!/usr/bin/python3
# Author: Shreyasta Samal
# -*- coding: utf-8 -*-
# @File : SarcGraphAnalysis.py


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import seaborn as sns

# Adding code to SarcGraphAnalysis

df = pd.read_csv('C:/Users/Shreyasta/PycharmProjects/Sarcomere/src/sub_df_1.csv', sep=",",header=None)
#df.columns=['Points', 'A', 'B', 'C', 'D']
#command to display maximum column width
#print(df.columns)
#df.drop(df.columns[[0,1,4,5]], axis=1)
pd.set_option("display.max_columns", None)

#print(df.drop(df.columns[[0,1,4,5]], axis=1))
xy_point_1 = df.drop(df.columns[[0,1,4,5]], axis=1)
#xy_point_1.columns = [xy_point_1.iloc[0], xy_point_1.iloc[1]]
xy_point_1 = xy_point_1.round(4)

xy_point_1 = xy_point_1[1:]
#xy_point_1 = xy_point_1.round(4)
#print(xy_point_1)
# Use df.columns command to drop columns via indexing
#pd.set_option('max_colwidth', None)
#pd.set_option('max_rows', None)


xy_point_1.rename(columns={2: 'x-coordinate', 3: 'y-coordinate'}, inplace=True)

print(xy_point_1.columns.values.tolist())
#xy_point_1.round({'x-coordinate': 2, 'y-coordinate': 2})
cols=['x-coordinate', 'y-coordinate']
#print(xy_point_1)

#
fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')

x = xy_point_1['x-coordinate']
y = xy_point_1['y-coordinate']
z = pd.Series(np.arange(1,322,1))
print((x))

ax.set_xlabel("x-coordinate")
ax.set_ylabel("y-coordinate")
#ax.set_zlabel("Number")

ax.scatter(x, y, s= 100)

plt.show()



#xy_point_1.plot(x=xy_point_1.iloc[:0], y=xy_point_1.iloc[:1], kind = 'scatter')
#plt.show()
#print(xy_point_1.columns.values.tolist())
#(xy_point_1)
# x= xy_point_1['x-coordinate']
# y= xy_point_1['y-coordinate']
# sns.scatterplot(data=xy_point_1, x="x-coordinate", y="y-coordinate")

#plt.plot(x,y)
#plt.show()


fig = plt.figure()
ax = fig.add_subplot(projection='3d')

# Grab some test data.
#X, Y, Z = axes3d.get_test_data(0.05)
X = pd.Series(np.arange(1,322,1))
Y = pd.Series(np.arange(1,322,1))
Z = pd.Series(np.arange(1,322,1))

# Plot a basic wireframe.
ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)

plt.show()