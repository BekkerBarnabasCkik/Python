#nap-típus-db

def beolvasas(fajl):
    f=open(fajl, "r", encoding="utf-8")
    t=f.readlines()
    f.close()
    joadatok=[]
    for i in range(len(t)):
        sor=t[i].strip().split()
        joadatok.append((int(sor[0]), sor[1], int(sor[2])))
    
    return joadatok

def kiiras(adatok):
    for i in range(len(adatok)):
        for j in range(len(adatok[i])):
            if j!=len(adatok[i])-1:
                print(adatok[i][j], end=", ")
            else:
                print(adatok[i][j])

def maxKivalasztas(adatok, hanyadiElem, poz):
    maxi=poz
    for i in range(poz+1, len(adatok), 1):
        if adatok[i][hanyadiElem]>adatok[maxi][hanyadiElem]:
            maxi=i
    
    return maxi

def rendezesCsokkenoen(adatok):
    for i in range(len(adatok)):
        maxi=maxKivalasztas(adatok, 1, i)
        seged=adatok[i]
        adatok[i]=adatok[maxi]
        adatok[maxi]=seged
    
    return adatok

def szamolas(adatok, hanyadikElem, vizsgalandoElem, LeMenteniElem):
    db=0
    maxdb=0
    elem=vizsgalandoElem
    maxelem=""
    for i in range(1, len(adatok), 1):
        if adatok[i][hanyadikElem]==elem:
            db+=1
        else:
            if db>maxdb:
                maxdb=db
                maxelem=adatok[i-1][LeMenteniElem]
            elem=adatok[i][hanyadikElem]
            db=0
    if db>maxdb:
        maxdb=db
        maxelem=adatok[i][LeMenteniElem]
        

    return maxelem

def miniKivalaszas2(adatok, adottElem, poz):
    mini=poz
    i=poz
    while i<len(adatok) and adatok[i][1]==adottElem:
        if adatok[i][2]<adatok[mini][2]:
            mini=i
        i+=1
    
    return mini

# def masodrendezes(adatok, hanyadikElem, nezettElem):
#     for i in range(len(adatok)):
#         mini=miniKivalaszas2(adatok, adatok[i][1], i)
#         seged=adatok[i]
#         adatok[i]=adatok[mini]
#         adatok[mini]=seged
    
#     return adatok

def utolsonap(adatok, relaciosJel):
    nap=adatok[0][0]
    for i in range(1, len(adatok), 1):
        if relaciosJel==">":
            if adatok[i][0]>nap:
                nap=adatok[i][0]
        else:
            if adatok[i][0]<nap:
                nap=adatok[i][0]    
    return nap

def szamolas2(adatok, mit, mennyi):
    db=0
    maxdb=0
    for i in range(len(adatok)):
        if adatok[i][0]==mit:
            db+=1
        else:
            maxdb+=db
            db=0
    if maxdb>mennyi:
        print(f"Ezen a npon összesen {maxdb} db volt")
    else:
        print(f"Nem volt annyi, csak {maxdb} db volt")

def TobbSzintuRendezes(adatok):
    for i in range(0, len(adatok)-1, 1):
        for j in range(i+1, len(adatok), 1):
            if adatok[i][2]<adatok[j][2] or (adatok[i][2]==adatok[j][2] and adatok[i][1]>adatok[j][1]):
                seged=adatok[i]
                adatok[i]=adatok[j]
                adatok[j]=seged
    
    return adatok

def szamolas3(t):
    db=0
    maxN=maxKivalasztas(t, 0, 0)
    if t[0][0]==maxN:
        db=1
    maxtipus=""
    maxdb=0
    for i in range(len(t)-1):
        if t[i][1]==t[i+1][1] and t[i][0]==maxN:
            db+=1
        if db>maxdb:
            maxdb=db
            maxtipus=t[i][1]
        if t[i][1]!=t[i+1][0]:
            db=1
            if t[i+1][0]==maxN:
                db=1
    
    return maxtipus

def minKivalasztas(adatok, hanyadiElem, poz):
    maxi=poz
    for i in range(poz+1, len(adatok), 1):
        if adatok[i][hanyadiElem]<adatok[maxi][hanyadiElem]:
            maxi=i
    
    return maxi

def szamolas4(t):
    db=0
    minN=minKivalasztas(t, 0, 0)
    if t[0][0]==minN:
        db=1
    mintipus=""
    mindb=10000
    for i in range(len(t)-1):
        if t[i][1]==t[i+1][1] and t[i][0]==minN:
            db+=1
        if db<mindb:
            mindb=db
            mintipus=t[i][1]
        if t[i][1]!=t[i+1][0]:
            db=1
            if t[i+1][0]==minN:
                db=1
    
    return mintipus

def main(fajl):
    adatok=beolvasas(fajl)
    kiiras(adatok)
    rendezettadatok=rendezesCsokkenoen(adatok.copy())
    kiiras(rendezettadatok)
    print(szamolas(rendezettadatok, 1, adatok[0][1], 1))
    kiiras(TobbSzintuRendezes(adatok.copy()))
    # print(utolsonap(adatok))

    # print("maxnap", szamolas(rendezettadatok, 0, utolsonap(rendezettadatok, ">"), 1))
    #-----------nem jó---------
    # print("minnap", szamolas(rendezettadatok, 0, utolsonap(rendezettadatok, "<"), 1))
    # -------------nem jó----------------
    print(szamolas3(adatok.copy()))
    print(szamolas4(adatok))
    nap=int(input())
    darabszam=int(input())
    szamolas2(rendezettadatok, nap, darabszam)
    print(szamolas(rendezettadatok, 1, rendezettadatok[0][1], 1))
main("rendel.txt")