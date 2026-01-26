import random

def tömbfeltöltes(hossz, honnan, meddig):
    t=[]
    for i in range(hossz):
        t.append(random.randint(honnan, meddig))
    
    return t

def kiiras(tömb):
    for i in range(len(tömb)):
        if i!=len(tömb)-1:
            print(tömb[i], end=",")
        else:
            print(tömb[i])
    
def masolas(tömb):
    t=[]
    for i in range(len(tömb)):
        t.append(tömb[i])
    
    return t

def Megszamolas(tömb, honnan, meddig):
    alkalmak=[]
    for i in range(honnan, meddig+1, 1):
        db=0
        for j in range(len(tömb)):
            if tömb[j]==i:
                db+=1
        alkalmak.append(db)

    return alkalmak

def Maximumkivalsztas(tömb):
    maxi=0
    for i in range(1, len(tömb), 1):
        if tömb[i]>tömb[maxi]:
            maxi=i

    return maxi+1


def allitas(j, nemszeretik, ki, i):
    return j<len(nemszeretik) and nemszeretik[j]!=ki[i]

def allitas2(j, nemszeretik):
    return j==(len(nemszeretik)) or len(nemszeretik)==0

def Eldontes(nemszeretik, ki, i):
    j=0
    while allitas(j, nemszeretik, ki, i):
        j+=1
    if allitas2(j, nemszeretik):
        nemszeretik.append(ki[i])

    return nemszeretik


def nemSzeretik(kit, ki, infotanar):
    nemszeretik=[]
    for i in range(len(kit)):
        if kit[i]==infotanar:
            nemszeretik=Eldontes(nemszeretik, ki, i)

    return nemszeretik

def feltetel3(j, nemszeretik, i):
    return j<len(nemszeretik) and nemszeretik[j]!=i

def eldontes2(nemszeretik, i, szeretik):
    j=0
    while feltetel3(j, nemszeretik, i):
        j+=1
    if j==len(nemszeretik):
        szeretik.append(i)

    return szeretik

def Szeretik(ki, kit, infotanar, honnan, meddig):
    szeretik=[]
    nemszeretik=nemSzeretik(kit, ki, infotanar)
    for i in range(honnan, meddig+1, 1):
        szeretik=eldontes2(nemszeretik, i, szeretik)

    return szeretik

def main():
    hossz=int(input())
    ki=tömbfeltöltes(hossz, 1, 20)
    kit=tömbfeltöltes(hossz, 1, 10)
    ki2=masolas(ki)
    kiiras(ki)
    kiiras(kit)
    talalatok=Megszamolas(kit, 1, 10)
    kiiras(talalatok)
    maxi=Maximumkivalsztas(talalatok)
    print(f"Az informatika tanár nem más mint az {maxi}. sorszámú ember")
    kiiras(Szeretik(ki, kit, maxi, 1, 20))

main()