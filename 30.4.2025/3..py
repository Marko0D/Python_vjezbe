##from math import*
##def racunanje_opsega_povrsine_trokuta(a,b,c):
##    o=a+b+c
##    s=(a+b+c)/2
##    p=sqrt(s*(s-a)*(s-b)*(s-c))
##    return "Opseg trokuta iznosi:", o, ", a površina iznosi", p
##a=int(input("Unesi duljinu stranice a trokuta:"))
##b=int(input("Unesi duljinu stranice b trokuta:"))
##c=int(input("Unesi duljinu stranice c trokuta:"))
##print(racunanje_opsega_povrsine_trokuta(a,b,c))
##def racunanje_opsega_povrsine_kruga(r):
##    o=2*r*3.14
##    p=r*r*3.14
##    return "Opseg iznosi", o, ", a površina iznosi", p
##r=int(input("Unesi duljinu polumjera kruga:"))
##print(racunanje_opsega_povrsine_kruga(r))
def racunanje_opsega_povrsine_kvadrata(a):
    o=4*a
    p=a*a
    return "Opseg iznosi", o, ", a površina iznosi", p
a=int(input("Unesi duljinu stranice kvadrata:"))
print(racunanje_opsega_povrsine_kvadrata(a))
