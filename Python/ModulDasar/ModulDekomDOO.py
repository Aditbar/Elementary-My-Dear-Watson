import sys
import numpy as np
import ModulTukarElemen as Menukar

#Pivoting
def DekomDOO(A, b, eps=1.0e-12):
    n = len(A[0])
    pivot = np.array(range(n))
    
    s = np.zeros(n)
    for i in range(n):
        s[i] = max(np.abs(A[i,:]))
        
    for k in range(0, n-1):
        p = np.argmax(abs(A[k:n, k])/s[k:n])+k
        if abs(A[p, k]) < eps:
            print("Matriks Singular\n")
            sys.exit("Time to go home")
            
        if p != k:
            Menukar.TukarBaris(b, k, p)
            Menukar.TukarBaris(s, k, p)
            Menukar.TukarBaris(A, k, p)
            
    print("Setelah pertukaran, Matriks A menjadi:\n", A)
    print("Vektor b menjadi:\n", b)
    print("Dan Vektor s menjadi:\n", s)
    input("Press Enter")

#Dekomposisi
    U = A.copy()
    L = np.identity(n)
    
    for k in range(0, n-1):
        for i in range(k+1, n):
            if U[i, k] != 0.0:
                L[i, k] = U[i, k]/U[k, k]
                for j in range(k, n):
                    U[i, j] = U[i, j] - (L[i, k]*U[k, j])
    return L, U, pivot

def SolusiDOO(L, U, b, pivot):
    n = len(b)
    z = b.copy()
    
    for i in range(n):
        z[i] = b[pivot[i]]
        
    y = np.zeros(n)
    x = np.zeros(n)
    y[0] = z[0]
    
    for k in range(1, n):
        y[k] = z[k]-np.dot(L[k, 0:k], y[0:k])
        
    x[n-1] = y[n-1]/U[n-1, n-1]
    for k in range(n-2, -1, -1):
        x[k] = (y[k]-np.dot(U[k, k+1:n], x[k+1:n]))/U[k, k]
        
    return x