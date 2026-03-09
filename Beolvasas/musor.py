def Beolvasas(fajl):
    f=open(fajl, "r", encoding="utf-8")
    t=f.readlines()
    f.close()
    adatok=[]
    for i in t:
        i=i.strip().split()
        print(i)
        
        adatok.append((int(i[0]), int(i[1]), int(i[2]), osszefuzes(i[3:])))
    
    return adatok

def osszefuzes(adat):
    joadat=""
    for i in range(len(adat)):
        joadat+=str(adat[i])+" "
    
    return joadat

def kiiras(adatok):
    for i in adatok:
        for j in range(len(i)):
            print(i[j], end=" ")
        print()

def rendezes(adatok):
    modositottAdatok=[]
    for i in range(len(adatok)):
        modositottAdatok.append((adatok[i], adatok[i][1]*60+adatok[i][2]))
    
    return modositottAdatok

def maximumrendezes(adatok):
    for i in range(len(adatok)):
        maxi=maximumKivalasztas(adatok, i)
        seged=adatok[i]
        adatok[i]=adatok[maxi]
        adatok[maxi]=seged
    
    return adatok

def maximumKivalasztas(adatok, i):
    maxi=i
    for j in range(i+1, len(adatok)):
        if adatok[j][len(adatok[j])-1]>adatok[maxi][len(adatok[maxi])-1]:
            maxi=j
    
    return maxi


def main(fajl):
    adatok=Beolvasas(fajl)
    kiiras(adatok)
    rendezettCsokkenoen=maximumrendezes(rendezes(adatok))
    kiiras(rendezettCsokkenoen)



main("musor.txt")