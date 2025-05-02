from collections import Counter
def izracunaj_statistiku_ocjena(lista_ocjena):
    najmanja=min(lista_ocjena)
    najveca=max(lista_ocjena)
    zbroj=0
    for ocjena in lista_ocjena:
        zbroj=zbroj+ocjena
    prosjek=zbroj/len(lista_ocjena)
    broj_pojavljivanja = Counter(lista_ocjena)
    return "Prosječna ocjena je", round(prosjek,2), "najveća ocjena je", najveca, ", a najmanja", najmanja, broj_pojavljivanja
lista=[1,2,3,3,2,4,1]
print(izracunaj_statistiku_ocjena(lista))
