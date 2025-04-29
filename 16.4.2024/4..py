def zbroj_znamenki(broj):
    zbroj=0
    tekst=str(broj)
    for i in tekst:
        zbroj=zbroj+int(i)
    return zbroj
print(zbroj_znamenki(123))
print(zbroj_znamenki(9876))
