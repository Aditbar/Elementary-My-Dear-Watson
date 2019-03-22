# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 07:08:56 2018

@author: Raditya Nugraha
"""

import numpy as np
import sys
import sympy as sym

def KoefLagr(datax, datay):
    if len(datax) != len(datay):
        sys.exit("Keep moving")
    n = len(datax)
    d = np.ones(n)
    c = np.ones(n)
    for j in range(n):
        for k in range(n):
            if k != j:
                d[j] *= (datax[j] - datax[k])
            c[j] = datay[j]/d[j]
    return c

def HitungLagr(datax, c, xx):
    n = len(datax)
    m = len(xx)
    p = np.zeros(m)
    t = np.ones(n)
    for i in range(m):
        for j in range(n):
            t[j] = 1
            for k in range(n):
                if j != k:
                    t[j] *= (xx[i] - datax[k])
            p[i] += t[j]*c[j]
    return p

def PoliLagr(datax, c):
    n = len(datax)
    x = sym.symbols('x')
    p = 0
    for j in range(n):
        t = 1
        for k in range(n):
            if j != k:
                t *= (x - datax[k])
        p += c[j]*t
    return(sym.cancel(p)).evalf(n = 4)