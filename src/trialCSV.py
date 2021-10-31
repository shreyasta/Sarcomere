#!/usr/bin/python3
# Author: Shreyasta Samal
# -*- coding: utf-8 -*-
# @File : trialCSV.py



import csv

with open('sarcomere.csv', 'w', newline='') as csvfile:
    fieldnames = ['frame_num','a', 'b', 'c', 'd']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'frame_num': '1', 'a': '123', 'b':'456', 'c':'789', 'd':'012'})
    writer.writerow({'frame_num': '2', 'a': '3', 'b':'4', 'c':'79', 'd':'54'})
    writer.writerow({'frame_num': '3', 'a': '12', 'b':'6', 'c':'78', 'd':'34'})

# import csv
# with open('eggs.csv', 'w', newline='') as csvfile:
#     spamwriter = csv.writer(csvfile, delimiter=',')
#     spamwriter.writerow(['Spam'] * 2 + ['Baked Beans'])
#     spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])