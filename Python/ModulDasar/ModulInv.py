# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 18:04:22 2018

@author: Raditya Nugraha
"""

import numpy as np
from ModulDekomDOO import DekomDOO, SolusiDOO

def InvMat(A):
    n = len(A[0])
    InvA = np.identity((n))
    
    L, U, pivot = DekomDOO(A, b)
    for k in range(n):
        y, InvA[:,k] = SolusiDOO(L, U, InvA[:,k], pivot)
        
    return InvA