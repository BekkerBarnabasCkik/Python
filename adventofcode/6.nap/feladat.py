def Beolvasa(fajl):
    f=open(fajl)
    f2=open(fajl)
    hossz=hosszmeghatarozas(f2)
    t=f.read()
    f.close()
    f2.close()
    elojelek=[]
    szamok=[]
    ertek=""
    for i in t:
        i=i.strip()
        if i!="" and i!="+" and i!="*":
            ertek+=str(i)
        elif i=="+" or i=="*":
            elojelek.append(i)
        elif ertek!="":
            szamok.append(int(ertek))
            ertek=""
    return szamok, elojelek, hossz

def hosszmeghatarozas(tömb):
    t=tömb.readline()
    eredmenyek=[]
    ertek=""
    for i in t:
        i=i.strip()
        if i!="":
            ertek+=str(i)
        elif ertek!="":
            eredmenyek.append(int(ertek))
            ertek=""

    return len(eredmenyek)    

def feladat(szamok, elojelek, hossz):
    osszeredmeny=0
    for i in range(hossz):
        eredmeny=0
        elojel=elojelek[i]
        if elojel=="*":
            eredmeny=1
        osszeredmeny+=osszegSzorzat(szamok, hossz, elojel,i, eredmeny)

    return osszeredmeny

def összeadas(eredmeny, szamok, j, hossz, i):
    eredmeny+=szamok[(j*hossz)+(i%hossz)]

    return eredmeny

def szorzas(eredmeny, szamok, j, hossz, i):
    eredmeny*=szamok[(j*hossz)+(i%hossz)]

    return eredmeny

def osszegSzorzat(szamok, hossz, elojel, i, eredmeny):
    for j in range(len(szamok)//hossz):
        if elojel=="+":    
            eredmeny=összeadas(eredmeny, szamok, j, hossz, i)
        else:
            eredmeny=szorzas(eredmeny, szamok, j, hossz, i)

    return eredmeny


def main(fajl):
    eredmenyek=Beolvasa(fajl)
    szamok=eredmenyek[0]
    elojelek=eredmenyek[1]
    hossz=eredmenyek[2]

    print(feladat(szamok, elojelek, hossz))


main("proba.txt")