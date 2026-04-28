import random

def randomedzo():
    t=["Venus", "Serena", "Rischard", "Oracene", "Pail Cohe", "Rick Macci"]
    vsz=random.randint(0, 999)
    osszeg=vsz%10+vsz//10%10+vsz//100
    return vsz, t[osszeg%len(t)].lower()

def edzesterv(nap):
    t=[]
    for i in range(1, nap+1, 1):
        if i%3==0:
            t.append(i**2+50)
        else:
            t.append(i**2)
    
    return t

def main():
    vsz, nev=randomedzo()
    print(vsz, nev)

    nap=int(input())
    edzesT=edzesterv(nap)
    print(edzesT)