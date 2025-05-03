def opseg(x,y):
    o=2*x+2*y
    return o
def povrsina(x,y):
    p=x*y
    return p
a1=int(input("unesi duljinu stranice a: "))
b1=int(input("unesi duljinu stranice b: "))
print("opseg prvog pravokutnika je: ",opseg(a1,b1),
      ", a povrsina je: ", povrsina(a1,b1))
a2=int(input("unesi duljinu stranice a: "))
b2=int(input("unesi duljinu stranice b: "))
print("opseg drugog pravokutnika je: ",opseg(a2,b2),
      ", a povrsina je: ", povrsina(a2,b2))
if(opseg(a1,b1)<opseg(a2,b2) and povrsina(a1,b1)<povrsina(a2,b2)):
    print("Prvi pravokutnik manji je opsegom i površinom")
elif(opseg(a1,b1)<opseg(a2,b2) and povrsina(a1,b1)>povrsina(a2,b2)):
    print("prvi pravokutnik manji je opsegom, ali je veći površinom")
elif(opseg(a1,b1)>opseg(a2,b2) and povrsina(a1,b1)<povrsina(a2,b2)):
    print("drugi pravokutnik manji je opsegom, ali je veći površinom")
elif(opseg(a1,b1)>opseg(a2,b2) and povrsina(a1,b1)<povrsina(a2,b2)):
    print("drugi pravokutnik manji je opsegom i površinom")
elif(opseg(a1,b1)==opseg(a2,b2) and povrsina(a1,b1)<povrsina(a2,b2)):
    print("pravokutnici su jednaki opsegom, ali je drugi pravokutnik veći površinom")
elif(opseg(a1,b1)==opseg(a2,b2) and povrsina(a1,b1)>povrsina(a2,b2)):
    print("pravokutnici su jednaki opsegom, ali je drugi pravokutnik manji površinom")
elif(opseg(a1,b1)>opseg(a2,b2) and povrsina(a1,b1)==povrsina(a2,b2)):
    print("pravokutnici su jednaki površinom, ali je prvi pravokutnik veći opsegom")
elif(opseg(a1,b1)<opseg(a2,b2) and povrsina(a1,b1)==povrsina(a2,b2)):
    print("pravokutnici su jednaki površinom, ali je prvi pravokutnik manji opsegom")
else:
    print("pravokutnici su jednaki opsegom i površinom")
