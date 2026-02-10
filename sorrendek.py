import math
import random

def Szamlalas(sorozathossz, kiirtszamok, kiirtsorozatok, i):
    db=0
    jodb=0
    for j in range(sorozathossz):
        if kiirtszamok[j]==kiirtsorozatok[i][j]:
            db+=1
    if db==len(kiirtszamok):
        jodb+=1
    
    return jodb

def BenneVanVizsgalat(kiirtsorozatok, kiirtszamok, sorozathossz):
    db=0
    jodb=0
    for i in range(len(kiirtsorozatok)):
        jodb+=Szamlalas(sorozathossz, kiirtszamok, kiirtsorozatok, i)

    if jodb!=0:
        return False
    else:
        return True

def SzamsorozatGeneralas(t):
    kiirtszamok=[]
    for j in range(len(t)):
        kivSzam=random.randint(0, len(t)-1)
        szam=t[kivSzam]
        k=0
        while k<len(kiirtszamok) and szam!=kiirtszamok[k]:
            k+=1
        if k==len(kiirtszamok):
            kiirtszamok.append(szam)
    return kiirtszamok

def Vizsgalat2(kiirtszamok, t, kiirtSorozatok):
    return len(kiirtszamok)==len(t) and BenneVanVizsgalat(kiirtSorozatok, kiirtszamok, len(t))

def joSzamsorozat(kiirtSorozatok, i, t):
    while len(kiirtSorozatok)==i:
        kiirtszamok=SzamsorozatGeneralas(t)
        if Vizsgalat2(kiirtszamok, t, kiirtSorozatok):
            print(kiirtszamok)
            kiirtSorozatok.append(kiirtszamok)
    
    return kiirtSorozatok


def Feladat():
    t=[1,2,3,4]
    kiirtSorozatok=[]
    for i in range(math.factorial(len(t))):
        kiirtSorozatok=joSzamsorozat(kiirtSorozatok, i, t)

    return kiirtSorozatok

def Main():
    print(len(Feladat()))

Main()
