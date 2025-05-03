def zbroj_znamenki(broj):
    zbroj=0
    for i in str(broj):
        zbroj=zbroj+int(i)
    return zbroj
print(zbroj_znamenki(123)) # Treba ispisati: 6
print(zbroj_znamenki(9876)) # Treba ispisati: 30
