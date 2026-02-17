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
    adatok={}
    for i in t:
        t=SorBeolvasas(i)
        adatok[t[0]]=t[1]
    
    return adatok

def megnezes(adatok, keresett, keresendo, db, tiltott, hova):
    kimenetek=adatok[keresett]
    print(adatok)
    for i in range(len(kimenetek)):
        if kimenetek[i]!=hova and kimenetek[i]!=tiltott and kimenetek[i]!="out" and kimenetek[i]!=" ":
            keresendo.append(kimenetek[i])
        elif kimenetek[i]==hova:
            db+=1
            print(db)
    
    return keresendo, db
    
def vegigmenes(adatok, kiindulas, tiltott, hova, regidarab):
    keresendo=[]
    db=0
    keresendo=adatok[kiindulas]
    adatok.pop(kiindulas)
    while len(keresendo)!=0:
        keresett=keresendo[0]
        keresendo.pop(0)
        keresendo, db=megnezes(adatok, keresett, keresendo, db, tiltott, hova)
        print(len(keresendo))
    
    if regidarab>db:
        return regidarab
    else:
        return db

def lehetoseg1(adatok):
    db=0
    db=vegigmenes(adatok, "svr", "dac", "fft", db)
    print(db)
    db=vegigmenes(adatok, "fft", "out", "dac", db)
    print(db)
    db=vegigmenes(adatok, "dac", "fft", "out", db)

    return db

def lehetoseg2(adatok):
    db=0
    db=vegigmenes(adatok, "svr", "fft", "dac", db)
    db=vegigmenes(adatok, "dac", "", "fft", db)
    db=vegigmenes(adatok, "fft", "dac", "out", db)

    return db

def Feladat(adatok, fajl):
    db=0
    # for i in range(2):
    db+=lehetoseg1(adatok)
    # db+=lehetoseg2(fajlbeolvasas(fajl))

    return db

def main(fajl):
    adatok=fajlbeolvasas(fajl)
    print(Feladat(adatok, fajl))

main("proba.txt")