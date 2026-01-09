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

def összeadas(szamok):
    eredmeny=0
    for i in range(len(szamok)):
        eredmeny+=szamok[i]

    return eredmeny

def szorzas(szamok):
    eredmeny=1
    for i in range(len(szamok)):
        eredmeny*=szamok[i]

    return eredmeny

def allitasOsszeadas(elojel, joszamok, j, max, i):
    return elojel=="+" and len(joszamok[j])>=max-i

def allitasSzorzas(elojel, joszamok, j, i):
    return elojel=="*" and len(joszamok[j])>i

def hozzarendelesOsszeadas(joszamok, i, j, max):
    return str(joszamok[j][max-1-i])

def hozzarendelesSzorzas(joszamok, j, i):
    return str(joszamok[j][len(joszamok[j])-1-i])

def ertekekMeghatarozas(joszamok, elojel, i, ertekek, max):
    ertek=""
    for j in range(len(joszamok)):
        if allitasOsszeadas(elojel, joszamok, j, max, i):
            ertek+=hozzarendelesOsszeadas(joszamok, i, j, max)
        elif allitasSzorzas(elojel, joszamok, j, i):
            ertek+=hozzarendelesSzorzas(joszamok, j, i)
    if ertek!="":    
        ertekek.append(int(ertek))
    
    return ertekek

def összegMeghatarozas(elojel, ertekek):
    if elojel=="+":
        return összeadas(ertekek)
    else:
        return szorzas(ertekek)

def Kiszamolas(elojelek, oszlop, joszamok, max):
    ertekek=[]
    elojel=elojelek[len(elojelek)-1-oszlop]
    for i in range(max):
        ertekek=ertekekMeghatarozas(joszamok, elojel, i, ertekek, max)
    print(ertekek)
    
    return összegMeghatarozas(elojel, ertekek)
    
def alapJoszam(alapszamok, hossz, joszamok, oszlop):
    for i in range(len(alapszamok)//hossz):
        joszamok.append(str(alapszamok[hossz-oszlop+i*hossz-1]))

    return joszamok

def SzamMeghatarozas(alapszamok, hossz, oszlop, elojelek):
    összeredmeny=0
    joszamok=[]
    joszamok=alapJoszam(alapszamok, hossz, joszamok, oszlop)
    max=maximum(joszamok)
    összeredmeny=Kiszamolas(elojelek, oszlop, joszamok, max)
    
    print(összeredmeny)

    return összeredmeny

def maximum(joszamok):
    max=len(str(joszamok[0]))
    for i in range(1, len(joszamok), 1):
        if len(str(joszamok[i]))>max:
            max=len(str(joszamok[i]))

    return max

def Feladat(alapszamok, hossz, elojelek):
    összeredmeny=0
    for i in range(hossz):
        összeredmeny+=SzamMeghatarozas(alapszamok, hossz, i, elojelek)
        print(összeredmeny)
    return összeredmeny

def main(fajl):
    eredmenyek=Beolvasa(fajl)
    szamok=eredmenyek[0]
    elojelek=eredmenyek[1]
    hossz=eredmenyek[2]

    print(Feladat(szamok, hossz, elojelek))
    # print("hossz")
    # print(hossz)
    # print(len(elojelek))



main("be.txt")