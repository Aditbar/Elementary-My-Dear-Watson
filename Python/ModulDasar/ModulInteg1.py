# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 17:06:15 2018

@author: Raditya Nugraha
"""

##Integrasi 1 Segmen
def trapz1data(h, f0, f1):
    I = h*((f0 + f1)/2)
    return I

##Integrasi n Segmen
def trapzndata(f, h, n):
    m = len(f) - 1
    sum = f[0]
    for i in range(1, m):
        sum += 2*f[i]
    sum = sum + f[m]
    I = sum*(h/2)
    return I

##Integrasi 1 Fungsi
def trapz1fungsi(f, a, b):
    h = b - a
    I = h*((f(a) + f(b))/2)
    return I

##Integrasi n Fungsi
def trapznfungsi(f, n, a, b):
    h = (b - a)/n
    x = a
    sum = f(a)
    for i in range(n - 1):
        x = x + h
        sum += 2*f(x)
    sum += f(b)
    I = (b - a)*(sum/(2*n))
    return I

