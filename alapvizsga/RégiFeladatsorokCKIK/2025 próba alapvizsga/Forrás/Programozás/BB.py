import random

def randomMI():
    MIk=["gemini", "chatGPT", "deepSpeek", "copilot"]
    szam=random.randint(0, 999)
    nullak=0
    if len(str(szam))!=3:
        nullak+=3-(len(str(szam)))
    for i in range(len(str(szam))):
        if str(szam)[i]=="0":
            nullak+=1
    
    return MIk[nullak].upper(), szam, nullak




def fibonacci(hossz):
    elemek=[0, 1]
    for i in range(1, hossz-1, 1):
        elemek.append(elemek[i]+elemek[i-1])

    print(elemek)
    return elemek

def PanikAModell(tomb):
    for i in range(len(tomb)):
        if tomb[i]%2!=0:
            tomb[i]=tomb[i]*3-1
        else:
            tomb[i]//=2
    print(tomb)
    return tomb

def Eldont(tomb):
    hossz=len(tomb)
    for i in range(len(tomb)-1):
        if tomb[i]-hossz<=tomb[i+1]:
            return True
    
    return False

def beolvasas(fajl):
    f=open(fajl, "r", encoding="UTF-8")
    t=f.readlines()
    f.close()
    adatok=[]
    elsosor=t[0]
    for i in range(1, len(t)):
        sor=t[i].strip().split()
        adatok.append((sor[0], sor[1], int(sor[2])))
    
    return adatok

def Rendezes(tomb):
    for i in range(len(tomb)):
        mini=i
        for j in range(i+1, len(tomb), 1):
            if tomb[j][0]<tomb[mini][0]:
                mini=j
        seged=tomb[i]
        tomb[i]=tomb[mini]
        tomb[mini]=seged
        print(tomb[i])
    
    return tomb

def Megszamolas(tomb):
    db=0
    oktAzo=""
    for i in range(len(tomb)):
        if oktAzo!=tomb[i][0]:
            db+=1
            oktAzo=tomb[i][0]
    
    return db

def maximumKivalasztas(tomb):
    maxi=0
    maxe=0
    ertek=0
    adottnev=""
    for i in range(len(tomb)):
        if tomb[i][0]==adottnev:
            ertek+=tomb[i][2]
        else:
            if ertek>maxe:
                maxe=ertek
                maxi=i
            ertek=tomb[i][2]
            adottnev=tomb[i][0]

    return maxi, maxe

def main():
    elem, szam, nullak=randomMI()
    print(f"GEnerált száma: {szam}, nullak száma {nullak}, a legjobb MI: {elem.lower()}")
    hossz=int(input())
    while hossz<2:
        hossz=int(input())
    NormalFibonacci=fibonacci(hossz)
    PanikFibonacci=PanikAModell(NormalFibonacci.copy())
    if Eldont(PanikFibonacci):
        print(f"Igen, volt olyan, amikor a csökkenés mértéle legalább {hossz}")
    else:
        print(f"Nem volt olyan amikor a csökkenés legalább {hossz}")

    BeolvasottAdatok=beolvasas("stat.txt")
    RendezettTomb=Rendezes(BeolvasottAdatok.copy())
    db=Megszamolas(RendezettTomb)
    print(f"{db} különböző oktatási azonosító szerepel a fájlban")
    maxi, maxe=maximumKivalasztas(RendezettTomb)
    print(f"A {RendezettTomb[maxi][0]} azonosítóval rendelekező diák töltött legtöbb időt az MI-vel: {maxe} óra")

main()