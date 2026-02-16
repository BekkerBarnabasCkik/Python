def Honnan(adat):
    return adat.strip(":")[:3]

def Hova(adat):
    adatok=adat.split(" ")
    adatok.pop(0)
    joadatok=[]
    for i in adatok:
        joadatok.append(i[:3])
    return joadatok

def SorBeolvasas(sor):
    adottSor=[]
    adottSor.append(Honnan(sor))
    adottSor.append(Hova(sor))

    return adottSor

def fajlbeolvasas(fajl):
    f=open(fajl)
    t=f.readlines()
    f.close()
    adatok=[]
    for i in t:
        adatok.append((SorBeolvasas(i)))
    
    return adatok

def Kereses(mit, miben, hanyadik):
    for i in range(len(miben)):
        if mit==miben[i][hanyadik]:
            hely=i
    return hely

def megnezes(adatok, keresett, megkeresettek, keresendo, db):
    kimenetek=adatok[Kereses(keresett, adatok, 0)][1]
    for i in range(len(kimenetek)):
        if kimenetek[i]!="out":
            keresendo.append(kimenetek[i])
        elif kimenetek[i]=="out":
            db+=1
    
    return keresendo, db
    



def Feladat(adatok):
    keresendo=[]
    keresett=""
    megkeresett=[]
    db=0
    keresendo=adatok[Kereses("you", adatok, 0)][1]
    print(keresendo)
    while len(keresendo)!=0:
        keresett=keresendo[0]
        keresendo.pop(0)
        keresendo, db=megnezes(adatok, keresett, megkeresett, keresendo, db)

    return db

def main(fajl):
    adatok=fajlbeolvasas(fajl)
    print(Feladat(adatok))

main("proba.txt")