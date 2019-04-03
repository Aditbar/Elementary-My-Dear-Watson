import numpy as np
from ModulPolNewt import HtgNewt, KoefNewt, PolNewt

datax = np.array([0.0, np.pi/4, np.pi/2])
datay = np.array([1, 0.70711, 0])
c = KoefNewt(datax, datay)
print("Koefisien:", c)

g = PolNewt(datax, c)
print("p = ", g)

xx = np.pi/3
yy = HtgNewt(datax, c, xx)
print("y = {:.4f}".format(yy))
