# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 17:42:43 2018

@author: Raditya Nugraha
"""

import numpy as np
from ModulDekomDOO import DekomDOO

A = np.array([[5, 3], \
              [2, 4]], float)

pivotasli = np.arange(len(A))
L, U, pivot = DekomDOO(A, b)

print("Hasil Dekomposisi adalah:\n")
print("Matriks L:\n ", L)
print("Matriks U:\n ", U)

if tuple(pivotasli) != tuple(pivot):
    print("Ada Pertukaran")
    
determinan = 1.0
for k in range(len(A)):
    determinan *= U[k, k]
    
print("Determinan A adalah:", determinan)