import numpy as np
from ModulElimGauss import ElimGauss
from math import sin, cos

S = 20

A = np.array([[1, -4, 3, 0, 0], \
              [0, 3, -8, 5, 0], \
              [0, 0, 5, -12, 7], \
              [0, 0, 0, 7, -16], \
              [0, 0, -10, 41, -54]], float)
b = np.array([-0.08*S, -0.16*S, -0.24*S, (-0.32*S) - 2, (-0.4*S) - 23], float)
 
x = ElimGauss(A, b, eps = 10**-3)
print("Solusinya adalah: \n")
for i in range(len(b)):
    print("x{:1d} = {:5.2f}".format(i+1, x[i]))

