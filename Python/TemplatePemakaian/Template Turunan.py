import numpy as np
from ModulTurunanPert import Diff1Forw, Diff1Mid, Diff1Back, Diff1Rich

x = 3
h = 1

def f(x):
    return 2*(x**2)

D = Diff1Mid(f, x, h)
print(D)

dh1 = Diff1Mid(f, 3, 1) 
dh2 = Diff1Mid(f, x, h/2) 
F = Diff1Rich(dh1, dh2, 2) 
print(F)