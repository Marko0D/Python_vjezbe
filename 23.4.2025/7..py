def filtriraj_po_duljini(lista,broj):
    nova_lista=[]
    for rijec in lista:
        if len(rijec)>broj:
            nova_lista.append(rijec)
    return nova_lista
rijeci = ["pas", "mačka", "miš", "slon", "žirafa"]
print(filtriraj_po_duljini(rijeci, 3))
