#!/usr/bin/python3
# Author: Shreyasta Samal
# -*- coding: utf-8 -*-
# @File : SarcGraph.py

import numpy as np
import pandas as pd
import plotly as pt
import csv

#TODO: load the txt file(done)
#TODO: load all the parameters in pandas(done)
#TODO: Give all param header names a,b,c,d(done)
#TODO: aggregate all the parameters, find min and max, (I can use groupby, then use min and max from this set)
#TODO: USe plots to get the min and max of all the values
#TODO: Just focus on min na d max of A,B as a tuple and mark it a graph
#TODO: Then repeat for C,D


df = pd.read_csv('C:/Users/Shreyasta/PycharmProjects/Sarcomere/src/resources/images/sarcomere/A_25/A_25_cropped_new_test.txt', sep=",")
df.columns=['Points', 'A', 'B', 'C', 'D']
pd.set_option('max_colwidth', None)
pd.set_option('max_rows', None)
print(df.head())
# This file has 8667 rows, and 27 points, so 8667/27 = 321, therefore every point has 321 rows
#framewise_grouping = df.groupby('Frame')
df.groupby("Points").apply(lambda x: x.to_csv(f"A_25_{x.name}.csv"))
#print(framewise_grouping.head())

# x =[]
# for key, value in framewise_grouping:
#     x = value.astype(str)
#     #print(type(x))
#     print(key)
#
# print(type(x))



# def get_group(g, key):x
#     if key in g.groups: return g.get_group(key)
#     return pd.DataFrame()
#
# get_group(df, '1')
#my_dict = {'1': 'aaa', '2': 'bbb', '3': 'ccc'}
#with open('A25_1_values.csv', 'w') as f:
# for key, value in framewise_grouping:
#     print((value))
        #f.write("%s\n"%(value))




#for key, value in framewise_grouping:
    #with open("C:/Users/Shreyasta/PycharmProjects/Sarcomere/src/resources/images/sarcomere/A_25/A_25_point_1.txt", "a+") as file_object:

        #visualize what parameters are coming in the end

        #file_object.write(value)


    #print(value.describe())