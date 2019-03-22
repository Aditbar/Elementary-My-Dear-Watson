# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 17:18:06 2018

@author: Raditya Nugraha
"""

from ModulInteg1 import trapz1data, trapz1fungsi, trapzndata, trapznfungsi
import numpy as np
import math as m
from math import exp

def Integran(x):
    return 2*x

h = 6
a = 0
b = 6
f0 = Integran(0)
f1 = Integran(6)
x = np.arange(0, 6, 1)

Integral0 = trapz1data(h, f0, f1)
print("Hasilnya adalah: {:5.4f}".format(Integral0))
    
Integral1 = trapzndata(Integran(x), 0.5, 100)
print("Hasilnya adalah {:5.4f}".format(Integral1))

Integral2 = trapz1fungsi(Integran, a, b)
print("Hasilnya adalah:{:5.4f}".format(Integral2))

Integral3 = trapznfungsi(Integran, 6, a, b)
print("Hasilnya adalah:{:5.4f}".format(Integral3))
