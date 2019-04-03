def TinggiRoket(t):
    for t in range(0, 60):
        if t < 15:
            y = 38.1454*t + 0.13743*((t)**3)
        
        elif 15 <= t <= 33:
            y = 1036 + 130.909*(t-15) + 6.18425*((t-15)**2) - 0.428*((t-15)**3)
        
        else:
            y = 2900 - 62.468*(t-33) - 16.9274*((t-33)**2) + 0.41796*((t-33)**3)
        
        return y

print(TinggiRoket(t))