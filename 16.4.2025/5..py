def izdvoji_parne(lista_brojeva):
    lista_parnih=[]
    for i in lista_brojeva:
        if i%2==0:
            lista_parnih.append(i)
    return lista_parnih
print(izdvoji_parne([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) # Treba ispisati: [2, 4, 6, 8, 10]
