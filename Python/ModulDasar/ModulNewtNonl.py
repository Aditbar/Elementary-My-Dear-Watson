# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 18:24:26 2018

@author: Raditya Nugraha
"""

import numpy as np
from ModulElimGauss import ElimGauss
import math

def newtnonl(f, x, akurasi = 1.0e-9):
    def jacobian(f, x):
        h = 1.0e-4
        n = len(x)
        jac = np.zeros((n, n))
        f0 = f(x)
        for i in range(n):
            temp = x[i]
            x[i] = temp + h
            f1 = f(x)
            x[i] = temp
            jac[:, i] = (f1-f0)/h
        return jac, f0
    for i in range(30):
        jac, f0 = jacobian(f, x)
        if math.sqrt(np.dot(f0, f0)/len(x)) < akurasi:
            return x
        dx = ElimGauss(jac, -f0)
        x = x+dx
        if math.sqrt(np.dot(dx, dx)) < akurasi*max(max(abs(x)), 1.0):
            return x
        print ("Too Much")
        