import matplotlib.pyplot as mplt
import numpy as np
from ModulPolLagr import KoefLagr, HitungLagr, PoliLagr

datax = np.array([1, 1.01, 1.02, 1.03, 1.04])
datay = np.array([2.4, 2.403, 3.386, 3.882, 2.906])

c = KoefLagr(datax, datay)
print("Koef Lagrange:")
for i in range(len(c)):
    print("c{:1d} = {:.4f}".format(i, c[i]))
    
Pn = PoliLagr(datax, c)
print("Polinomialnya adalah:", Pn)

xx = np.linspace(1, 1.04, 100)
p = HitungLagr(datax, c, xx)
#for i in range(len(xx)):
    #print("Nilai Pn({:.4f}) = {:.2f}".format(xx[i], p[i]))

mplt.plot(xx, p, '-')
mplt.grid(True)
mplt.xlabel("Time at Minutes")
mplt.ylabel("T Rate")
mplt.show()