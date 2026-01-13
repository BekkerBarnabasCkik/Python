import random

ertek=int(input())

def ForintbeAtvaltas(ertek):
    if ertek%3==0:
        Forint=ertek*0.713
        print(Forint)
 
    else:
        print(f"Ez az ertek: {ertek} nem osztható 3-al")
ForintbeAtvaltas(ertek)


def kockadobas():
    return random.randint(1,12)

kock1=kockadobas()
kock2=kockadobas()
kock1=3
kock2=2
print(kock1, kock2)

def Prime(kock1, kock2):
    osszeg=kock1+kock2
    if osszeg!=1 and osszeg%2!=0:
        i=3
        while i<osszeg//2 and osszeg%i!=0:
            i+2
        if i>=osszeg//2:
            if kock1>kock2: 
                print("Nyert" , kock1)
            else:
                print("Nyert", kock2)
        else:
            print("Nem prímszám")
    else:
        print("Nem prímszám")
        
Prime(kock1, kock2)

def Feladat():
    f=open("adatok.txt")
    t=f.read()
    f.close()
    ertekek=[]
    ertek=""
    for i in t:
        i=i.strip()
        if i!="":
            ertek+=i
        else:
            ertekek.append(int(ertek)) 
            ertek=""   

    maxi=0

    for i in range(1, len(ertekek), 1):
        if ertekek[i]>ertekek[maxi]:
            maxi=i
    
    print(f"{len(ertekek)-maxi+1} éve volt a legnépesebb a törzs")

    return ertekek

def NegyvenAlatt(ertekek):
    i=0
    while i<len(ertekek) and ertekek[i]>=40:
        i+=1
    if i<len(ertekek)-1:
        print(f"Volt olyían év, hogy 40 alá esett a népesség. {len(ertekek)-i+1} éve")

ertekek=Feladat()
print(ertekek)
NegyvenAlatt(ertekek)