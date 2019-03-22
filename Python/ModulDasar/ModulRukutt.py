# -*- coding: utf-8 -*-
"""
Created on Wed May 30 20:49:08 2018

@author: Raditya Nugraha
"""

import numpy as np

def rukut4(F, x, y, xAkhir, h):
    def rk4(F, x, y, h):
        K0 = h*F(x, y)
        K1 = h*F(x + h/2.0, y + K0/2.0)
        K2 = h*F(x + h/2.0, y + K1/2.0)
        K3 = h*F(x + h, y + K2)
        return (K0 + 2.0*K1 + 2.0*K2 + K3)/6.0
    X = []
    Y = []
    X.append(x)
    Y.append(y)
    while x < xAkhir:
        h = min(h, xAkhir - x)
        y = y + rk4(F, x, y, h)
        x = x + h
    X.append(x)
    Y.append(y)
    return np.array(X), np.array(Y)

def rukut3(F, x, y, xAkhir, h):
    def rk3(F, x, y, h):
        K0 = h*F(x, y)
        K1 = h*F(x + h/2.0, y + K0/2.0)
        K2 = h*F(x + h, y - K0*h + 2*K1*h)
        return (K0 + 4.0*K1 + K2)/6.0
    X = []
    Y = []
    X.append(x)
    Y.append(y)
    while x < xAkhir:
        h = min(h, xAkhir - x)
        y = y + rk3(F, x, y, h)
        x = x + h
    X.append(x)
    Y.append(y)
    return np.array(X), np.array(Y)