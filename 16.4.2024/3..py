def je_palindrom(rijec):
    if rijec==rijec[::-1]:
        return True
    else:
        return False
print(je_palindrom("radar"))
print(je_palindrom("Python"))
