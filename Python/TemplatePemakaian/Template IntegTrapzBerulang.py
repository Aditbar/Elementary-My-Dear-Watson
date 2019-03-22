# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 08:13:06 2018

@author: Raditya Nugraha
"""

from ModulTrapzBerulang import trapznB
from math import exp
import numpy as np
import math as m

def integran(x):
    return 2*x

a = 0
b = 10
x = np.arange(0, 6, 1)
f = integran(x)
k = 6
akurasi = 0.001
segmen = 1
Integral = trapznB(integran, a, b, akurasi, segmen)

print("Hasilnya Adalah = {:5.4f}".format(Integral))