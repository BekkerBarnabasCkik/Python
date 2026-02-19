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

def bennevane(honnan, hova, miben):
    i=0
    while i<len(miben) and (miben[i][0]!=honnan and miben[i][1]!=hova):
        i+=1
    return i==len(miben)

def UtvonalakNoveles(keresendo, kimenet, utvonalakszama):
    i=0
    while i<len(keresendo) and keresendo[i]!=kimenet:
        i+=1
    if i<len(keresendo):
        utvonalakszama[i]+=1
    else:
        utvonalakszama.append(utvonalakszama[0])
    
    return utvonalakszama

def Megszmolas_Hozzafuzes(kimenetek, i, hova, tiltott, megkeresettek, keresendo, keresett, db, utvonalakszama):
    if kimenetek[i]!=hova and kimenetek[i]!=tiltott and kimenetek[i]!="out" and kimenetek[i]!=" ":
        megkeresettek.append((keresett, kimenetek[i]))
        utvonalakSzama=UtvonalakNoveles(keresendo, kimenetek[i], utvonalakszama)
        keresendo.append(kimenetek[i])
    elif kimenetek[i]==hova:
        db+=1
    
    return db, megkeresettek, keresendo

def megnezes(adatok, keresett, keresendo, db, tiltott, hova, megkeresettek, utvonalakszama):
    kimenetek=adatok[keresett]
    for i in range(len(kimenetek)):
        if bennevane(keresett, kimenetek[i], megkeresettek):
            db, megkeresettek, keresendo=Megszmolas_Hozzafuzes(kimenetek, i, hova, tiltott, megkeresettek, keresendo, keresett, db, utvonalakszama)
    
    return keresendo, db, megkeresettek
    


def vegigmenes(adatok, kiindulas, tiltott, hova, regidarab):
    keresendo=[]
    megkeresettek=[]
    db=0
    utvonalakSzama=[1]
    keresendo=adatok[kiindulas]
    adatok.pop(kiindulas)
    while len(keresendo)!=0:
        keresett=keresendo[0]
        keresendo.pop(0)
        keresendo, db, megkeresettek=megnezes(adatok, keresett, keresendo, db, tiltott, hova, megkeresettek, utvonalakSzama)
    if db>1:
        return db
    else:
        return 0

def lehetoseg1(adatok):
    db=0
    db+=vegigmenes(adatok, "svr", "dac", "fft", db)
    print(db)
    db+=vegigmenes(adatok, "fft", "out", "dac", db)
    print(db)
    db+=vegigmenes(adatok, "dac", "fft", "out", db)
    print(db)

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