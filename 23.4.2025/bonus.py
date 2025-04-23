def je_anagram(string1,string2):
    prvi="".join(string1.lower().split())
    drugi="".join(string2.lower().split())
    if len(prvi)!=len(drugi):
        return False
    else:
        return sorted(prvi)==sorted(drugi)
print(je_anagram("Listen", "Silent"))
print(je_anagram("Hello", "World"))
