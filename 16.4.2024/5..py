def izdvoji_parne(lista):
    lista_parnih=[]
    for broj in lista:
        if broj%2==0:
            lista_parnih.append(broj)
    return lista_parnih
print(izdvoji_parne([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
