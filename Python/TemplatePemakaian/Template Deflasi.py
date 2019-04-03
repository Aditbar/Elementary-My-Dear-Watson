import numpy as np
from ModulLaguere import DefPol

a = np.array([12, -2, -48, -10, 3])
r = 6.0
deflate = DefPol(a, r)
print('Koefisien P(n-1) adalah:\n')

for i in range(len(deflate)):
    print('b{:1d} = {:12.5f}'.format(i, deflate([i])))