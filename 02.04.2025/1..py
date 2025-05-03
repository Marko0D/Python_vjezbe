def zbroj(x,y):
    return x+y
a=int(input("Unesi prvi broj:"))
b=int(input("Unesu drugi broj:"))
x=zbroj(a,b)
c=int(input("Unesi treći broj:"))
d=int(input("Unesi četvrti broj:"))
y=zbroj(c,d)
print("Zbroj unesenih brojeva je", zbroj(x,y))
