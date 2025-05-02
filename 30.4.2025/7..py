import string
import random
def generiraj_lozinku(duljina):
    odabiri=list(string.ascii_lowercase + string.ascii_uppercase +
             string.digits + string.printable)
    lozinka=""
    for i in range(duljina):
        i=random.choice(odabiri)
        lozinka=lozinka+str(i)
    return lozinka
print(generiraj_lozinku(10))
