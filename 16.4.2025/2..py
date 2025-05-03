def pronadji_min_max(lista):
    najmanji=min(lista)
    najveci=max(lista)
    return najmanji, najveci
min_broj, max_broj = pronadji_min_max([23, 55, 2, 88, 15, 7])
print("Najmanji broj u listi je:", min_broj, ", a najveći je", max_broj)
