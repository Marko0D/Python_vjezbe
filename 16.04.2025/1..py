def osnovne_operacije(a,b):
    suma=a+b
    razlika=a-b
    umnozak=a*b
    if b==0:
        kolicnik="Nije moguće dijeliti s nulom!"
    else:
        kolicnik=a/b
    return suma, razlika, umnozak, kolicnik
a=int(input("Unesi prvi broj:"))
b=int(input("Unesi drugi broj:"))
print(osnovne_operacije(a,b))
