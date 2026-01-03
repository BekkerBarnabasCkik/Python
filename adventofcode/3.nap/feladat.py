def Fajlbeolvasas(fajl):
    f=open(fajl)
    t=f.read()
    f.close() 
    ertekek=[]
    ertek=0
    for i in t:
        i=i.strip()
        if i!="":
            ertekek.append(int(i))

    return ertekek

def Hosszusag(fajl):
    hossz=0
    f=open(fajl)
    t=f.read()
    f.close()
    for i in t:
        i=i.strip()
        if i!="":
            hossz+=1
        else:
            hossz=0

    return hossz

def vegpont(i, hossz):
    return ((i+1)//hossz+1)*hossz

def maximum(tizes, ertekek,max, hossz, i):
    for j in range(i+1,vegpont(i, hossz),1):
        ertek=tizes+ertekek[j]
        if ertek>max:
            max=tizes+ertekek[j]

    return max

def feladat(ertekek, hossz):
    osszes=0
    max=0
    for i in range(0, len(ertekek), 1):
        tizes=ertekek[i]*10
        if (i+1)%hossz!=0:
            max=maximum(tizes, ertekek, max, hossz, i)
        else:
            osszes+=max
            max=0
    print(osszes)
    
    return max

def main():
    t=Fajlbeolvasas("Be.txt")
    hossz=Hosszusag("Be.txt")
    feladat(t, hossz)

main()