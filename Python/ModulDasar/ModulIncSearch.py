# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 11:05:39 2018

@author: Raditya Nugraha
"""

from numpy import sign

def IncS(f, a, b, dx):
    x1 = a
    f1 = f(x1)
    x2 = a + dx
    f2 = f(x2)
    while sign(f1) == sign(f2):
        if x1 >= b:
            return None, None
        x1 = x2
        f1 = f2
        x2 = x2 + dx
        f2 = f(x2)
    else:
        return x1, x2