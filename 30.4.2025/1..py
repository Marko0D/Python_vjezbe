def izracunaj_popust(cijena,postotak):
    postotak=postotak/100
    iznos=cijena*postotak
    nova=cijena-cijena*postotak
    return "Iznos popusta je:", iznos, ",a nova cijena je", nova
a=int(input("Unesi cijenu proizvoda:"))
b=int(input("Unesi postotak popusta(bez znaka %):"))
print(izracunaj_popust(a,b))
