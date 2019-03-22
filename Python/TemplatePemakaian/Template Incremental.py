# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 11:10:49 2018

@author: Raditya Nugraha
"""

from ModulIncSearch import IncS
import math

w = 5.5
l = 160
h = 15

def f(x):
    return x*(math.cosh((w*l)/(2*x)) - 1) - w*h

x1 = 1
x2 = 1200

for i in range(4):
    dx = (x2 - x1)/10.0
    x1, x2 = IncS(f, x1, x2, dx)
    
x = (x1 + x2)/2.0
print("Akarnya adalah = {:6.6f}".format(x))