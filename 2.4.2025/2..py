def opseg(x,y):
    o=2*x+2*y
    return o
def povrsina(x,y):
    p=x*y
    return p
a=int(input("Unesi duljinu stranice a pravokutnika:"))
b=int(input("Unesi duljinu stranice b pravokutnika:"))
print("Opseg pravokutnika je", opseg(a,b), ", a površina je", povrsina(a,b))
