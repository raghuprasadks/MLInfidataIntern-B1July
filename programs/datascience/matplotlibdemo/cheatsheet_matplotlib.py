# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 13:38:01 2020

@author: lenovo
"""


import numpy as np
x = np.linspace(0, 10, 100)
y = np.cos(x)
z = np.sin(x)


data = 2 * np.random.random((10, 10))
data2 = 3 * np.random.random((10, 10))
Y, X = np.mgrid[-3:3:100j, -3:3:100j]
U = -1 - X**2 + Y
V = 1 + X - Y**2
from matplotlib.cbook import get_sample_data
img = np.load(get_sample_data('axes_grid/bivariate_normal.npy'))