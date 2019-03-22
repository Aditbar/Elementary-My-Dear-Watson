# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 06:51:58 2018

@author: Raditya Nugraha
"""

import sys
import numpy as np
import ModulTukarElemen as Menukar

#Pertukaran
def ElimGauss(A, b, eps=1.0e-12):
    n = len(b)
    s = np.zeros(n)
    for i in range(n):
        s[i] = max(np.abs(A[i,:]))
        
    for k in range(0, n-1):
        p = np.argmax(abs(A[k:n, k])/s[k:n])+k
        if abs(A[p, k]) < eps:
            print("Matriks Singular\n")
            sys.exit("Time to go home")
            
        if p != k:
            Menukar.TukarBaris(b, k, p)
            Menukar.TukarBaris(s, k, p)
            Menukar.TukarBaris(A, k, p)
            
    print("Setelah pertukaran, Matriks A menjadi:\n", A)
    print("Vektor b menjadi:\n", b)
    print("Dan Vektor s menjadi:\n", s)
    input("Press Enter")
#Mulai Eliminasi    
    for k in range(0, n-1):
        for i in range(k+1, n):
            if A[i, k] != 0.0:
                lam = A[i, k]/A[k, k]
                for j in range(k, n):
                    A[i, j] = A[i, j] - (lam*A[k, j])
                b[i] = b[i] - (lam*b[k])
                print("Setelah Eliminasi, matriks A menjadi:\n", A)
                print("Dan b menjadi:\n", b)
                
    x = np.zeros(n)
    x[n-1] = b[n-1]/A[n-1, n-1]
    for k in range(n-2, -1, -1):
        x[k] = (b[k]-np.dot(A[k, k+1:n], x[k+1:n]))/A[k, k]
    return x