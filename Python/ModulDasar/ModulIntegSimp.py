# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 17:48:54 2018

@author: Raditya Nugraha
"""

import sys

def simp13D(f, h):
    if len(f) < 3:
        sys.exit("Minimal 3 Data")
    I = h*(f[0] + 4*f[1] + f[2])/3
    return I

def simp38D(f, h):
    if len(f) < 4:
        sys.exit("Minimal 4 Data")
    I = 3*h*(f[0] + 3*f[1] + 3*f[2] + f[3])/8
    return I

def simp13F(f, a, b):
    h = (b - a)/2
    c = (b + a)/2
    I = h*(f(a) + 4*f(c) + f(b))/3
    return I

def simp13nF(f, a, b, n):
    if (n%2) != 0:
        sys.exit("Segmen Harus Genap")
    h = (b - a)/n
    x = a
    sum = f(x)
    for i in range(1, n - 2, 2):
        x += h
        sum += 4*f(x)
        x += h
        sum += 2*f(x)
    x += h
    sum += 4*f(x)
    sum += f(b)
    I = (b - a)*sum/(3*n)
    return I