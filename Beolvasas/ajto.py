#első sor: taratlmazza, hogy hány elem van
#többi sor: óra perc azonosító irány

#1. feladat: tároljuk le az adatokat
#2. feladat: írjuk ki az adatokat
#3. feladat: ki volt az utolsó aki be ment
#4. feladat: a vizsgáld időszak végén hányan maradtak bent
#5. feladat: Az azonosítók 1-50 közötti számok, kik azok, aki nem
#mentek se ki, se be
#6. feladat: Ki az, aki a legtöbbször ment be az ajtón

def feltoltes(n):
    t=[]
    for i in range(n):
        sor=input()
        adatok=sor.split(' ')
        t.append( (int(adatok[0]),int(adatok[1]),
                   int(adatok[2]),adatok[3]) )
    return t

def kiir(t):
    for i in range(len(t)):
        ora,perc,azon,irany=t[i]
        print(f"{ora}:{perc} {azon} {irany}")
#5. feladat
def benneVan(t, tul):
    i=0
    while i<len(t) and not t[i][2]==tul:
        i+=1
    return i<len(t)

def kivalogat(t):
    ki=[]
    for  i in range(1,51,1):
        if not benneVan(t,i):
            ki.append(i)
    return ki

#3. feladat
def linearisKereses(t,tul):
    i=len(t)-1
    while i>=0 and t[i][3]!=tul:
        i-=1
    if i>=0:
        return i
    else:
        return -1

def bentLevokSzama(t):
    db=0
    for _,_,_,irany in t:
        if irany=="be":
            db+=1
        else:
            db-=1
    return db

def megszamolas(t,tul):
    db=0
    for i in range(len(t)):
        if t[i][3]==tul:
            db+=1
    return db


def main():
    n=int(input())
    t=feltoltes(n)
    # t=[
    #     (9, 1, 2, "be"), 1
    #     (9, 1, 9, "be"), 2
    #     (9, 3, 15, "be"),3
    #     (9, 5, 9, "ki"), 2
    # ]
    kiir(t)
    print(kivalogat(t))
    index=linearisKereses(t,"be")
    if index>-1:
        print(f"Utolsó, aki bement: {t[index][2]}")
    else:
        print(f"Még senki sem hagyta el a társalgót!")
    print(f"Bentlévők száma: {bentLevokSzama(t)}")
    darab=megszamolas(t,"be")-megszamolas(t,"ki")
    print(f"Bentlévők száma: {darab}")
main()