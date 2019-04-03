import math as m
import sys
from numpy import sign

def bisect(f, x1, x2, cm = 0, eps = 1.0e-4):
    f1 = f(x1)
    if f1 == 0.0:
        return f1
    f2 = f(x2)
    if f2 == 0.0:
        return f2
    if sign(f1) == sign(f2):
        sys.exit("Not here")
    n = int(m.ceil(m.log(abs(x2-x1)/eps)/m.log(2.0)))
    
    for i in range(n):
        xm = 0.5*(x1+x2)
        fm = f(xm)
        if (cm == 1) and (abs(fm) > abs(f1)) and (abs(fm) > abs(f2)):
            return None
        if fm == 0:
            return fm
        if sign(f2) != sign(fm):
            x1 = xm
            f1 = fm
        else:
            x2 = xm
            f2 = fm
    return (x1+x2)/2.0