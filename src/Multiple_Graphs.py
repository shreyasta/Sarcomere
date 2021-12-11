#!/usr/bin/python3
# Author: Shreyasta Samal
# -*- coding: utf-8 -*-
# @File : Multiple_Graphs.py

import matplotlib.pyplot as plt
import numpy as np



x = [1, 2, 3, 4, 5]
y = [3, 3, 3, 3, 3]

x_1 = [6,7, 7,9, 8]
y_1 = [1, 4, 5, 2, 2]


# plot lines
plt.plot(x, y, label="line 1", linestyle="-")
plt.plot(y_1, x_1, label="line 2", linestyle="--")
plt.plot(x, np.sin(x), label="curve 1", linestyle="-.")
plt.plot(x, np.cos(x), label="curve 2", linestyle=":")
plt.legend()
plt.show()