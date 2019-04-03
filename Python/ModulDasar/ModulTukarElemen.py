def TukarBaris(v, i, j):
    if len(v.shape) == 1:
        v[i], v[j] = v[j], v[i]
    else:
        v[[i, j],:] = v[[j, i],:]
        
def TukarKolom(v, i, j):
    v [:, [i, j]] = v[:,[j, i]]