def broji_samoglasnike(string):
    broj_samoglasnika=0
    for i in string.lower():
        if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
            broj_samoglasnika=broj_samoglasnika+1
    return broj_samoglasnika
print(broji_samoglasnike("Python Programiranje")) # Treba ispisati: 6
