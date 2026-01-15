import random
n=int(input())

def TombFeltoltes(hanyszor, mettol, meddig):
    t=[]
    for i in range(hanyszor):
        t.append(random.randint(mettol, meddig))
    
    return t

def Megszamlalas(tömb, mettol, meddig):
    alkalmak=[]
    for i in range(mettol, meddig+1, 1):
        db=0
        for j in range(len(tömb)):
            if tömb[j]==i:
                db+=1
        alkalmak.append(db)

    return alkalmak

def MaximumKivalasztas(tömb):
    maxi=0
    for i in range(1, len(tömb), 1):
        if tömb[i]>tömb[maxi]:
            maxi=i
    
    return maxi

def main(n):
    ki=TombFeltoltes(n, 1, 20)
    print(ki)
    kit=TombFeltoltes(n, 1, 10)
    print(kit)
    alkalmak=Megszamlalas(kit, 1, 10)
    print(alkalmak)
    print(MaximumKivalasztas(alkalmak)+1)

main(n)

