# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 18:32:46 2018

@author: Raditya Nugraha
"""

import numpy as np
from ModulNewtNonl import newtnonl

def f(x):
    f = np.zeros(len(x))
    f[0] = (8.21 - x[0])**2 + (0.01 - x[1])**2 - x[2]**2
    f[1] = (0.34 - x[0])**2 + (6.62 - x[1])**2 - x[2]**2
    f[2] = (5.96 - x[0])**2 + (-1.12 - x[1])**2 - x[2]**2
    return f

x = np.array([1.0, 1.0, 1.0])
solusi = newtnonl(f, x)
print("Solusinya adalah:\n")
for i in range(len(solusi)):
    print('x{:1d} = {:5.2f}'.format(i, solusi[i]))