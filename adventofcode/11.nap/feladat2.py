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

def megnezes(adatok, keresett, megkeresettek, keresendo):
    kimenetek=adatok[Kereses(keresett, adatok, 0)][1]
    for i in range(len(kimenetek)):
        if kimenetek[i]!="out":
            keresendo.append(kimenetek[i])
    
    return keresendo

def megnezesdb(adatok, keresett, megkeresettek, keresendo, db):
    kimenetek=adatok[Kereses(keresett, adatok, 0)][1]
    for i in range(len(kimenetek)):
        if kimenetek[i]!="out":
            keresendo.append(kimenetek[i])
        elif kimenetek[i]=="out":
            db+=1
    
    return keresendo, db

def vegigmanes2(adatok, mibol):
    keresendo=[]
    keresett=""
    megkeresett=[]
    db=0
    keresendo=adatok[Kereses(mibol, adatok, 0)][1]
    print(keresendo)
    while len(keresendo)!=0:
        keresett=keresendo[0]
        keresendo.pop(0)
        keresendo, db=megnezesdb(adatok, keresett, megkeresett, keresendo, db)
        print("vegigmenes2")

    return db

def vegigmanes(adatok, mit, mibol):
    keresendo=[]
    keresett=""
    megkeresett=[]
    db=0
    keresendo=adatok[Kereses(mibol, adatok, 0)][1]
    print(keresendo)
    while len(keresendo)!=0:
        keresett=keresendo[0]
        keresendo.pop(0)
        if keresett==mit:
            db=vegigmanes2(adatok, mit)
        keresendo=megnezes(adatok, keresett, megkeresett, keresendo)
        print("vegigmenes1")

    return db

def Feladat(adatok):
    keresendo=[]
    keresett=""
    megkeresett=[]
    db=0
    keresendo=adatok[Kereses("svr", adatok, 0)][1]
    print(keresendo)
    while len(keresendo)!=0:
        keresett=keresendo[0]
        keresendo.pop(0)
        if keresett=="dac":
            db+=vegigmanes(adatok, "fft", "dac")
        elif keresett=="fft":
            db+=vegigmanes(adatok, "dac", "fft")
        keresendo,_=megnezesdb(adatok, keresett, megkeresett, keresendo, db)

    return db

def main(fajl):
    adatok=fajlbeolvasas(fajl)
    print(Feladat(adatok))

main("be.txt")