def pretvori_sekunde(sekunde):
    minute=sekunde//60
    sec=sekunde%60
    sati=minute//60
    mm=minute%60
    return sati, "sata", mm, "minuta", sec, "sekundi."
a=int(input("Unesi vrijeme u sekundama:"))
print(pretvori_sekunde(a))
