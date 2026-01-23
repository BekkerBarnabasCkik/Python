import random

def szerencse():
    szam=random.randint(1, 40)

    if szam%2!=0:
        return szam/2
    else:
        return (szam+1)/2

print(f"Béla vagyok, szerencse számám a(z) {szerencse()}, kedvenc színem a piros.")

#2.feladat


def tabla(t, szam):
    t=[szam]
    for i in range(9):
        t.append(szam+(i+1)*5)

    return t

def Osszegzes(t):
    ertek=0
    for i in range(len(t)):
        if t[i]%3==0:
            ertek+=t[i]
    
    return ertek

def main()
    nev=str(input())
    szam=random.randint(2, 12)
    print=(f"név: {nev}")
    print(f"Felírt számok: {tabla(szam)}")
    print(Osszegzes(tabla(szam)))

# 3.feladat

    def Beolvasas(fajl)
        f=open(fajl)
        t=f.read()
        f.close()
        ertek=""
        szamolas=0
        for i in t:
            if i!="":
                ertek+=i
            elif ertek!="":
                if szamolas==0:
                    nevek.append(ertek)
                    szamolas+=1
                elif szamolas==1:
                    gyümölcs.append(ertek)
                    szamolas+=1
                else:
                    szam.append(int(ertek))
                    szamolas=0
        szamok.append(ertek)

        return  nevek, gyümölcs, szamolas

    nevek, gyümölcs, szamolas = Beolvasas("diakok.txt")

    infomax=0
    db=0
    for i in range(len(nevek)):
        print(f"{nevek[i]} {gyümölcs[i]} {szamok[i]}")
        if gyümölcs[i].lover()=="alma"
            almakedvelok.append(nevek[i])
        if szamok[i]>szamok[infomax]
            infomax=i
        if len(nevek[i])>7:
            db+=1
    print(f"Az alma kedvelők: {almakedvelok}")
    print(f"A legtöbb informatikai órajá egy {nevek[infomax]} ne4vű diáknak volt.")
    print(f"{db} diáknak hosszabb a neve 7 karakternél")
    