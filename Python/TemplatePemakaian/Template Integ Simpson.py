from ModulIntegSimp import simp13D, simp38D, simp13F, simp13nF
import numpy as np

def integran(x):
    return 2*x

h = 1.5
x = np.arange(0, 6, 1)
f = integran(x)
a = 0
b = 3
n = 8

Integral0 = simp13D(f, h)                           #Untuk 3 Titik
print("Hasilnya adalah = {:5.4f}".format(Integral0))

Integral1 = simp38D(f, h)                           #Untuk 4 Titik
print("Hasilnya adalah = {:5.4f}".format(Integral1))

Integral2 = simp13F(integran, a, b)
print("Hasilnya adalah = {:5.4f}".format(Integral2))

Integral3 = simp13nF(integran, a, b, n)
print("Hasilnya adalah = {:5.4f}".format(Integral3))