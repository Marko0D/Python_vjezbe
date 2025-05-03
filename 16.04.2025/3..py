def je_palindrom(rijec):
    if rijec[::-1]==rijec:
        return True
    else:
        return False
print(je_palindrom("radar")) # Treba ispisati: True
print(je_palindrom("Python")) # Treba ispisati: False
