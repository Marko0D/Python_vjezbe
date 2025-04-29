def broji_samoglasnike(string):
    zbroj=0
    for i in string.lower():
        if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
            zbroj=zbroj+1
    return zbroj
print(broji_samoglasnike("Python Programiranje"))
