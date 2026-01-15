def Fajlbeolvasas(fajl):
    f=open(fajl)
    f2=open(fajl)
    hossz=hosszmeghatarozas(f2)
    t=f.read()
    f.close()
    ertekek=[]
    for i in t:
        if i=="S" or i=="." or i=="^":
            ertekek.append(i.strip())

    return hossz, ertekek

def hosszmeghatarozas(tömb):
    t=tömb.readline()
    
    return len(t)-1

def main(fajl):
    ertekek=Fajlbeolvasas(fajl)
    hossz=ertekek[0]
    t=ertekek[1]
    feladat(hossz, t)

def SMeghatarozas(tömb):
    i=0
    while tömb[i]!="S":
        i+=1

    return i

def Lepesek(Spoz, tömb, hossz):
    db=0
    tömb[Spoz+hossz]="i"
    for i in range(hossz, len(tömb)-hossz, 1):
        if tömb[i]=="i":
            if tömb[i+hossz]=="^":
                if tömb[i+hossz-1]!="^":
                    tömb[i+hossz-1]="i"
                if tömb[i+hossz+1]!="^":
                    tömb[i+hossz+1]="i"
                db+=1
            else:
                tömb[i+hossz]="i"
    return db

def kiiras(tömb, hossz):
    print(tömb[0], end="")
    for i in range(1, len(tömb), 1):
        if (i+1)%hossz!=0:
            print(tömb[i], end="")
        else:
            print(tömb[i], end="\n")

def feladat(hossz, tömb):
    Spoz=SMeghatarozas(tömb)
    print(Lepesek(Spoz, tömb, hossz))

main("be.txt")