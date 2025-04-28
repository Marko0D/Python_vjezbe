def je_prost(broj):
    if broj<=1:
        return False
    for i in range(2, broj//2):
        if broj%i==0:
            return False
        return True
print(je_prost(7))
print(je_prost(8))
#ili ovako:
def je_prost(broj):
    brojac=0
    for i in range(broj,1,-1):
        if broj%i==0:
           brojac=brojac+1
    if brojac>2:
        return False
    else:
        return True
x=int(input("unesi broj"))
print(je_prost(x))
