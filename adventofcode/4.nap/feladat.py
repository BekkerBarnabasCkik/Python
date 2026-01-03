def Fajlbeolvasas(fajl):
    f=open(fajl)
    f2=open(fajl)
    t=f2.read()
    hossz=hosszmeghaítarozast(f)
    f.close()
    f2.close()
    ertekek=[]
    for i in t:
        i=i.strip()
        if i!="":
            ertekek.append(i)
    return ertekek, hossz

def hosszmeghaítarozast(tömb):
    hossz=len(tömb.readline())-1

    return hossz

def jobblent(elem, tömb, hossz):
    db=0
    if tömb[(elem+hossz)+1]=="@":
        db=1

    return db
def balLent(elem, tömb, hossz):
    db=0
    if tömb[elem+hossz-1]=="@":
        db=1

    return db
def lent(elem, tömb, hossz):
    db=0
    if tömb[elem+hossz]=="@":
        db=1

    return db
def fent(elem, tömb, hossz):
    db=0
    if tömb[elem-hossz]=="@":
        db=1

    return db
def jobbFent(elem, tömb, hossz):
    db=0
    if tömb[elem-hossz+1]=="@":
        db=1
    
    return db
def balFent(elem, tömb, hossz):
    db=0
    if tömb[elem-hossz-1]=="@":
        db=1
    
    return db
def jobb(elem, tömb):
    db=0
    if tömb[elem+1]=="@":
        db=1

    return db
def bal(elem, tömb):
    db=0
    if tömb[elem-1]=="@":
        db=1

    return db


def Fenti(elemek, hossz, tömb, db):

    if elemek%hossz!=0 and (elemek+1)%hossz!=0:
            db+=balFent(elemek, tömb, hossz)
            db+=jobbFent(elemek, tömb, hossz)

    else:
        if elemek%hossz!=0:
            db+=balFent(elemek, tömb, hossz)
        if (elemek+1)%hossz!=0:
            db+=jobbFent(elemek, tömb, hossz)
    
    db+=fent(elemek, tömb, hossz)

    return db

def Lenti(elemek, hossz, tömb, db):
    if elemek%hossz!=0 and (elemek+1)%hossz!=0:
        db+=balLent(elemek, tömb, hossz)
        db+=jobblent(elemek, tömb, hossz)

    else:
        if (elemek+1)%hossz!=0:
            db+=jobblent(elemek, tömb, hossz)
        if elemek%hossz!=0:
            db+=balLent(elemek, tömb, hossz)

    db+=lent(elemek, tömb, hossz)

    return db

def BalJobb(elemek, hossz, tömb, db):
    if elemek%hossz!=0 and (elemek+1)%hossz!=0:
        db+=bal(elemek, tömb)
        db+=jobb(elemek, tömb)

    else:
        if elemek%hossz!=0:
            db+=bal(elemek, tömb)
        elif elemek<len(tömb): 
            db+=jobb(elemek, tömb)

    return db

def meddig(sorok, hossz, tömb):
    return len(tömb)-(((len(tömb)-(sorok*hossz+hossz-1))//hossz)*hossz)

def Alkalom(elemek, hossz, tömb, alkalmak):
    db=0
    if elemek>=hossz:
        db=Fenti(elemek, hossz, tömb, db)

    if elemek<len(tömb)-hossz:
        db=Lenti(elemek, hossz, tömb, db)

    if db<4:
        db=BalJobb(elemek, hossz, tömb, db)
    if db<4:
        tömb[elemek]="."
        alkalmak+=1

    return alkalmak

def SorokonBelüliSzamlalas(sorok, hossz, tömb, alkalmak):
    for elemek in range(sorok*hossz, meddig(sorok, hossz, tömb),1):
        if tömb[elemek]=="@":
            alkalmak=Alkalom(elemek, hossz, tömb, alkalmak) 

    return alkalmak  

def feladat(tömb, hossz):
    alkalmak=0
    for sorok in range(0, len(tömb)//hossz, 1):
        alkalmak=SorokonBelüliSzamlalas(sorok, hossz, tömb, alkalmak)
    return alkalmak

def main(tömb, hossz):
    összalakom=feladat(tömb, hossz)
    alkalmak=összalakom
    while alkalmak>0:
        alkalmak=feladat(tömb, hossz)
        összalakom+=alkalmak
    return összalakom

ertekek=Fajlbeolvasas("be.txt")
t=ertekek[0]
hossz=ertekek[1]
print(main(t, hossz))



