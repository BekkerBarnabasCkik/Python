#elsősor- mennyi adó A-B-C
def Fajlbeolvasas(fajl):
    f=open(fajl, "r", encoding="utf-8")
    t=f.readlines()
    f.close()
    elsosor=t[0].split()
    A_ado=int(elsosor[0])
    B_ado=int(elsosor[1])
    C_ado=int(elsosor[2])
    elsosor=A_ado, B_ado, C_ado
    adatok=[]
    for i in range(1, len(t), 1):
        sor=t[i].strip().split()
        adatok.append((int(sor[0]), str(sor[1]), str(sor[2]), str(sor[3]), int(sor[4])))
    return adatok, elsosor

def kiiras(adatok):
    for i in range(len(adatok)):
        for j in range(len(adatok[i])):
            print(adatok[i][j], end=" ")
        print()

def kereses(mit, miben):
    i=0
    while mit!=miben[i]:
        i+=1
    
    return i

def kiszamolas(adatok, fizetes):
    joadatok=[]
    for i in range(len(adatok)):
        joadatok.append((adatok[i], fizetes[kereses(adatok[i][3], ["A", "B", "C"])]*adatok[i][4]))
    
    return joadatok

def maximumKivalasztas(adatok, i):
    maxi=i
    for j in range(i, len(adatok), 1):
        print(adatok[j])
        if adatok[j][1]>adatok[maxi][1]:
            maxi=j
        
    
    return maxi

def rendezes(adatok):
    seged=[]
    for i in range(len(adatok)-1):
        maxi=maximumKivalasztas(adatok, i)
        adatok[i]=seged
        adatok[i]=adatok[maxi]
        adatok[maxi]=seged

    return adatok

def main(fajl):
    adatok, elsosor=Fajlbeolvasas(fajl)
    kiiras(adatok)
    kiiras(rendezes(kiszamolas(adatok, elsosor)))
main("utca.txt")