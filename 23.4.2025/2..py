def broji_rijeci(recenica):
    br_rijeci=1
    for slovo in recenica:
        if slovo==" ":
            br_rijeci=br_rijeci+1
    return br_rijeci
broj=broji_rijeci("Python je zabavan programski jezik.")
print(broj)
