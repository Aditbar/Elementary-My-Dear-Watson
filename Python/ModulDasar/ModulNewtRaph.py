# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 11:15:36 2018

@author: Raditya Nugraha
"""

def NewtRaph(f, df, x, eps = 1.0e-9):
    for i in range(30):
        dx = -f(x)/df(x)
        x = x + dx
        if abs(dx) < eps:
            return x, 1
    print("Too much\n")