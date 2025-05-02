def fibonacci(n):
    niz=[0,1]
    if n<2:
        return niz[0]
    while len(niz)<n:
        sljedeci_broj=niz[-1]+niz[-2]
        niz.append(sljedeci_broj)
    return niz
print(fibonacci(10))
