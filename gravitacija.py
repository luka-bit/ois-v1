def gravitacija(visina: float) -> float:
    C = 6.674e-11
    M = 5.972e24
    r = 6.371e6
    return C*M / (r+visina)**2


def izpis(visina: float, pospesek: float):
    print("visina =", visina)
    print("pospesek =", pospesek)


visina = float(input("vnesi nadmorsko visino [m]: "))
izpis(visina, gravitacija(visina))

print("OIS je zakon!")
