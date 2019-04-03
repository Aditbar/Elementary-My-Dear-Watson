import numpy as np

def Euler(F, x, y, xakhir, h):
    X = []
    Y = []
    X.append(x)
    Y.append(y)
    while x < xakhir:
        h = min(h, xakhir, -x)
        y = y + h*F(x, y)
        x = x + h
        X.append(x)
        Y.append(y)
    return np.array(X), np.array(Y)

def ModEuler(F, x, y, xakhir, h):
    def rk_2euler(F, x, y, h):
        K0 = h*F(x, y)
        K1 = h*F(x + h/2.0, y + K0)
        return K1
    X = []
    Y = []
    X.append(x)
    Y.append(y)
    while x < xakhir:
        h = min(h, xakhir - x)
        y = y + rk_2euler(F, x, y, h)
        x = x + h
    X.append(x)
    Y.append(y)
    return np.array(x), np.array(y)
