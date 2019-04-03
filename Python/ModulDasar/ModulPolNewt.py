import sys
import sympy as sym

def HtgNewt(datax, a, xx):
    n = len(datax) - 1
    p = a[n]
    for k in range(1, n+1):
        p = a[n - k] + (xx - datax[n - k])*p
    return p

def KoefNewt(datax, datay):
    if len(datax) != len(datay):
        sys.exit("Selesai")
    m = len(datax)
    a = datay.copy()
    for k in range(1, m):
        a[k:m] = (a[k:m] - a[k - 1])/(datax[k:m] - datax[k-1])
    return a

def PolNewt(datax, a):
    x = sym.symbols('x')
    n = len(datax) - 1
    p = a[n]
    for k in range(1, n+1):
        p = a[n - k] + (x - datax[n - k])*p
    return sym.cancel(p).evalf(n = 4)

