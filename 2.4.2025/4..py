def savrsen(br):
    zbroj=0
    for i in range(1,br):
        if br%i==0:
            zbroj=zbroj+i
    if zbroj==br:
        return br
    else:
        return 0
kolicina_brojeva=0
i=0
while True:
    if kolicina_brojeva==4:
        break
    i=i+1
    b=savrsen(i)
    if b==i:
        print(b)
        kolicina_brojeva += 1
