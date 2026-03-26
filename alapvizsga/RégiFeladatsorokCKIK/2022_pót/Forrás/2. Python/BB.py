import math

#1. feladat
def atvaltas(szam):
    return szam*1.8+32

#2. feladat

def ÖsszesSzamitas(also, felso):
    osszes=0
    for i in range(also, felso+1, 1):
        osszes+=AdottSzamitas(i)
    
    return osszes

def AdottSzamitas(ertek):
    return 3*pow(ertek, 2)+4*ertek-7

def Beolvasas():
    f=open("lotto.txt")
    t=f.readlines()
    f.close()
    adatok=[]
    szamok=[]
    for i in range(len(t)): 
        sor=t[i].strip().split(";")
        if sor[0]!="":
            adatok.append((int(sor[0]), sor[1]))
            for j in range(2, len(sor)):
                szamok.append(int(sor[j]))
    
    return adatok, szamok

#3.feladat

def Legtobb(szamok):
    legtobbSzamok=[]
    maxe=0
    db=0
    kulonbozoSzamok=KIvalogatas(szamok)
    for i in range(len(kulonbozoSzamok)):
        db=0
        for j in range(len(szamok)):
            if szamok[j]==kulonbozoSzamok[i]:
                db+=1
        if db>maxe:
            maxe=db
            legtobbSzamok=[kulonbozoSzamok[i]]
        elif db==maxe:
            legtobbSzamok.append(kulonbozoSzamok[i])
    if db>maxe:
        maxe=db
        legtobbSzamok=[kulonbozoSzamok[i]]
        db=0
    elif db==maxe:
        legtobbSzamok.append(kulonbozoSzamok[i])

    return legtobbSzamok, maxe

def KIvalogatas(szamok):
    JoSzamok=[]
    for i in range(len(szamok)):
        j=0
        while j<len(JoSzamok) and JoSzamok[j]!=szamok[i]:
            j+=1
        
        if j==len(JoSzamok):
            JoSzamok.append(szamok[i])
    
    return JoSzamok

def Legkevesebb(szamok):
    legkevesebbSzamok=[]
    mine=0
    db=0
    kulonbozoSzamok=KIvalogatas(szamok)
    for i in range(len(kulonbozoSzamok)):
        db=0
        for j in range(len(szamok)):
            if szamok[j]==kulonbozoSzamok[i]:
                db+=1
        if db<mine:
            mine=db
            legkevesebbSzamok=[kulonbozoSzamok[i]]
        elif db==mine:
            legkevesebbSzamok.append(kulonbozoSzamok[i])
    
    if db<mine:
        mine=db
        legkevesebbSzamok=[kulonbozoSzamok[i]]
    elif db==mine:
        legkevesebbSzamok.append(kulonbozoSzamok[i])

    return legkevesebbSzamok, mine

def Eldontes(szamok):
    NemhuztakKi=[]
    for i in range(1, 91, 1):
        j=0
        while j<len(szamok) and i!=szamok[j]:
            j+=1
        
        if j!=len(szamok):
            NemhuztakKi.append(i)
    
    return NemhuztakKi  


def main():
    #1.feladat
    szam=int(input("C: "))
    Faren=atvaltas(szam)
    print(f"{szam} Celsius = {Faren} Farenheit")

    #2.feladat
    also=int(input("Alsó határ: "))
    felso=int(input("FElső határ: "))
    print(ÖsszesSzamitas(also, felso))
    adatok, szamok=Beolvasas()
    #3. feladat
    legtobbSzam, LegtobbDB=Legtobb(KIvalogatas(szamok))
    print(f"A legtöbbször {LegtobbDB} kihuzott szam(ok) {legtobbSzam}")
    legkevesebbSzam, legkevesebbDb=Legkevesebb(szamok)
    print(f"A legkevesebbszer {legkevesebbDb} kihuzott szam(ok) {legkevesebbSzam}")
    print(f"2021-ben egyszer sem húzták ki: {Eldontes(KIvalogatas(szamok))}")
main()