def je_valjana_email(email):
    if "@" in email and "." in email:
        return True
    else:
        return False
print(je_valjana_email("gnwogno@gmail.com"))
