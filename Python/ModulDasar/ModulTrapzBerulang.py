def trapznB(f, a, b, akurasi, segmen = 0):
    def trapznFB(f, a, b, k, lseb = 0.0):
        if k == 1:
            I = (f(a) + f(b))*(b - a)/2.0
        else:
            n = 2**(k - 2)
            h = (b - a)/n
            x = a + (h/2.0)
            sum = 0.0
            for i in range(n):
                sum = sum + f(x)
                x = x + h
            I = (lseb + h*sum)/2.0
        return I
    lseb = 0.0
    for k in range(1, 50):
        lsdh = trapznFB(f, a, b, k, lseb)
        if (k > 1) and (abs(lsdh - lseb)) < akurasi:
            break
        lseb = lsdh
    if segmen is not 0:
        print("Jumlah Segmen =", 2**(k - 1))
    return lsdh


