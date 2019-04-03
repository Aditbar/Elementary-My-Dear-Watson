import numpy as np

def err(DiffNum, Analitik):
    err = abs((DiffNum - Analitik)/Analitik)*100
    return err

def Diff1Back(f, x, h):
    D = (3*f(x) - 4*f(x - h) + f(x - 2*h))/(2*h)
    return D

def Diff1Forw(f, x, h):
    D = (-3*f(x) + 4*f(x + h) - f(x + 2*h))/(2*h)
    return D

def Diff1Mid(f, x, h):
    D = (f(x + h) - f(x - h))/(2*h)
    return D

def Diff1Rich(dh1, dh2, p):
    penyebut = 2**p - 1
    pembilang = ((2**p)*dh2) - dh1
    return pembilang / penyebut

def TurunanDat(x, h):
    a = len(x)
    f = np.zeros(a)
    f[0] = (-3*x[0] + 4*x[1] - x[2])/(2*h)
    f[a - 1] = (3*x[a - 1] - 4*x[a - 2] + x[a - 3])/(2*h)
    for i in range(1, a - 1):
        f[i] = (x[i + 1] - x[i - 1])/(2*h)
    return f

def TurunanKedua(x, h):
    a = len(x)
    f = np.zeros(a)
    f[0] = ((2*x[0]) - (5*x[1]) + (4*x[2]) - x[3])/(h**2)
    f[a - 1] = ((2*x[a - 1]) - (5*x[a - 2]) + (4*x[a - 3]) - x[a - 4])/(h**2)
    for i in range(1, a - 1):
        f[i] = (x[i + 1] - 2*x[i] + x[i - 1])/(h**2)
    return f