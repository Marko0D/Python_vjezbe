def osnovne_operacije(a,b):
    suma=a+b
    razlika=a-b
    umnozak=a*b
    if b==0:
        kolicnik="Nije moguće djeljenje s nulom."
    else:
        kolicnik=a/b
    return suma, razlika, umnozak, kolicnik
rezultat = osnovne_operacije(10,5)
print(rezultat)
