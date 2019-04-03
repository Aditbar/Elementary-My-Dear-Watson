def HtgPol(a, x):
    n = len(a) - 1
    p = a[n]
    dp = 0.0 + 0.0j
    ddp = 0.0 + 0.0j
    for i in range(1, n+1):
        ddp = ddp*x + 2.0*dp
        dp = dp*x + p
        p = p*x + a[n - i]
    return p, dp, ddp

def DefPol(a, r):
    n = len(a) - 1
    b = []
    b[n-1] = a[n]
    for i in range(n - 2, -1, -1):
        b[i] = a[1 + i] + r*b[i + 1]
    return b
