import random

#1.feladat
def szerencse():
    randomSzam=random.randint(1, 40)
    if randomSzam%2!=0:
        return randomSzam/2
    else:
        return (randomSzam+1)/2

#2. feladat

def tabla(t, szam):
    for i in range(10):
        t.append(szam+(i*5))
    
    return t

def osszegzes(t):
    osszes=0
    for i in range(len(t)):
        if t[i]%3==0:
            osszes+=t[i]

    return osszes

# 3.feladat

def Beolvasas():
    f=open("diakok.txt")
    t=f.readlines()
    f.close()
    adatok=[]
    for i in t:
        i=i.strip().split()
        adatok.append((i[0], i[1], int(i[2])))
    
    return adatok

def kivalogatas(t):
    almaszeretok=[]
    for i in range(len(t)):
        if t[i][1]=="alma":
            almaszeretok.append(t[i][0])

    return almaszeretok

def MaximumKivalasztas(t):
    maxi=0
    for i in range(1, len(t), 1):
        if t[i][2]>t[maxi][2]:
            maxi=i
    
    return maxi

def HosszuNev(t):
    db=0
    for i in range(len(t)):
        if len(t[i][0])>7:
            db+=1
    
    return db

def main():
    #1.feladat
    print(f"Béla vagyok, a szerencse számom a(z) {szerencse()}, a kedvenc színem a piros.")
    #2.feladat
    nev=str(input("Név: "))
    kezdoSzam=random.randint(2, 12)
    szamok=[]
    szamok=tabla(szamok, kezdoSzam)
    harmasSzamok=osszegzes(szamok)
    print(f"A felírt számok: {szamok}")
    print(f"A 3-mal osztható számok összege és név: {harmasSzamok} {nev}")
    #3.feladat
    adatok=Beolvasas()
    print(f"Az alma kedvelők: {kivalogatas(adatok)}")
    print(f"A legtöbb informatika órája  egy {adatok[MaximumKivalasztas(adatok)][0]} nevű diáknak volt")
    print(f"{HosszuNev(adatok)} diáknka hosszabb a neve 7 karakternél")



main()