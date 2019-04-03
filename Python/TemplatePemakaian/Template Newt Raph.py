from ModulNewtRaph import NewtRaph

def f(x):
    return x**3 - 10.0*(x)**2 + 5.0

def df(x):
    return 3.0*(x)**2 - 20.0*x

akar, iterasi = NewtRaph(f, df, 2.0)
print("Akarnya adalah = {:5.2f}".format(akar))
print("Banyak iterasi = {}".format(iterasi))