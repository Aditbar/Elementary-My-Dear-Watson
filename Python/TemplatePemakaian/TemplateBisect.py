from ModulBisect import bisect
import math

w = 5.5
l = 160
h = 15
lamb = w/1186.83

def f(x):
    return (2/lamb)*(math.sinh((lamb*l)/2)) - x

x1 = 160
x2 = 700

x = bisect(f, x1, x2, eps = 10**-3)
print("Akarnya adalah = {:6.6f}".format(x))