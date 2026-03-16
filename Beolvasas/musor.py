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

def EgyszeruCseresRendzes(adatok):
    for i in range(len(adatok)-1):
        for j in range(0, len(adatok)-1):
            if adatok[j+1][0]<adatok[j][0]:
                seged=adatok[j]
                adatok[j]=adatok[j+1]
                adatok[j+1]=seged
    
    return adatok

def atlagokSzamolasa(adatok):
    atlagok=[]
    adottAdo=adatok[0][0]
    hossz=0
    db=0
    for i in range(len(adatok)):
        if adatok[i][0]==adottAdo:
            hossz+=adatok[i][1]*60+adatok[i][2]
            db+=1
        else:
            hossz+=adatok[i][1]*60+adatok[i][2]
            atlagok.append(hossz/(db+1))
            db=0
            hossz=0
            adottAdo=adatok[i+1][0]
    hossz+=adatok[len(adatok)-1][1]*60+adatok[len(adatok)-1][2]
    atlagok.append(hossz/(db+1))

    return atlagok

def kereses(mit, hol):
    i=0
    while hol[i]!=mit:
        i+=1
    
    return i

def percszamitas(sor):
    return sor[1]*60+sor[2]

def ZenekLementese(zenek, UjZene):
    jozenek=[]
    for i in range(len(zenek)):
        jozenek.append(zenek[i])
    jozenek.append(UjZene)
    return jozenek


def MusorBlokk(adatok):
    Csatornak=[1, 2, 3]
    percek=[0, 0, 0]
    szamok=[(), (), ()]
    for i in range(len(adatok)):
        poz=kereses(adatok[i][0][0], Csatornak)
        if percek[poz]+percszamitas(adatok[i][0])<=60*60:
            percek[poz]+=percszamitas(adatok[i][0])
            szamok[poz]=ZenekLementese(szamok[poz], adatok[i][0][3])
    
    return szamok, percek

def LegnagyobbSzamok(adatok):
    szamok=[]
    perc=0
    i=0
    while perc<=60*60 and i<len(adatok):
        if adatok[i][0][0]==3:
            if perc+percszamitas(adatok[i][0])<60*60:
                perc+=percszamitas(adatok[i][0])
                szamok.append(adatok[i][0][3])
        i+=1
    
    return szamok, perc

def Eggyezik(regiAdatok, Ujadatok):
    for i in range(len(regiAdatok)):
        j=0
        while j<len(regiAdatok[i]) and regiAdatok[i][j]==Ujadatok[i][0][j]:
            j+=1
        if j==len(regiAdatok[i]):
            print(regiAdatok[i])

def main(fajl):
    adatok=Beolvasas(fajl)
    kiiras(adatok)
    rendezettCsokkenoen=maximumrendezes(rendezes(adatok))
    print(rendezettCsokkenoen)
    kiiras(rendezettCsokkenoen)
    print()
    RendezettAdoSzerint=EgyszeruCseresRendzes(adatok.copy())
    kiiras(RendezettAdoSzerint)
    print(atlagokSzamolasa(RendezettAdoSzerint))
    kiiras(MusorBlokk(rendezettCsokkenoen)[0])
    print(LegnagyobbSzamok(rendezettCsokkenoen)[0])
    Eggyezik(adatok, rendezettCsokkenoen)



main("musor.txt")