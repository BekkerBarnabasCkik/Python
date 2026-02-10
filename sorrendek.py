import math
import random

def Vizsgalat(kiirtsorozatok, kiirtszamok, sorozathossz):
    db=0
    jodb=0
    for i in range(len(kiirtsorozatok)):
        db=0
        for j in range(sorozathossz):
            if kiirtszamok[j]==kiirtsorozatok[i][j]:
                db+=1
        if db==len(kiirtszamok):
            jodb+=1
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

def Feladat():
    t=[1,2,3,5]
    kiirtSorozatok=[]
    for i in range(math.factorial(len(t))):
        while len(kiirtSorozatok)==i:
            kiirtszamok=SzamsorozatGeneralas(t)
            if len(kiirtszamok)==len(t):
                if Vizsgalat(kiirtSorozatok, kiirtszamok, len(t)):
                    print(kiirtszamok)
                    kiirtSorozatok.append(kiirtszamok)

    return kiirtSorozatok

def Main():
    print(len(Feladat()))

Main()
