import numpy as np
from ModulDekomDOO import DekomDOO, SolusiDOO

A = np.array([[-(12/5), 1, 0, 0], \
               [1, -(12/5), 1, 0], \
               [0, 1, -(12/5), 1], \
               [0, 0, 1, -(12/5)]], float)
b = np.array([-620, -120, -120, -320], float)

L, U, pivot = DekomDOO(A, b)

print("Hasil Dekomposisi adalah:\n")
print("Matriks L:\n", L, "\n")
print("Matriks U:\n", U, "\n")
print("Vektor pivot:\n", pivot, "\n")
input("Tekan Enter")

x = SolusiDOO(L, U, b, pivot)
print("Solusinya adalah: \n")
for i in range(len(b)):
    print("x{:1d} = {:5.2f}".format(i+1, x[i]))    