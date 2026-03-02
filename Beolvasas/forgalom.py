def feltoltes(fajl):
    t=[]
    f=open(fajl, "r", encoding="utf-8")
    sorok=f.readlines()
    hossz, seb=sorok[0].strip().split()
    for i in range(1, len(sorok)):
        adatok=sorok[i].strip().split()
        t.append((int(adatok[0]), int(adatok[1]), int(adatok[2]), int(adatok[3]), str(adatok[4])))
    
    return t, seb

def Egyszerurendezes(t):
    for i in range(0, len(t)-1, 1):
        for j in range(i+1, len(t), 1):
            if t[i][3]<t[j][3]:
                egyik=t[i]
                t[i]=t[j]
                t[j]=egyik
    
    return t

def maximumkivalasztas(i, t):
    maxi=i
    for j in range(i+1, len(t), 1):
        if t[j][0]>t[maxi][0]:
            maxi=j

    return maxi

def maximumRendezes(t):
    for i in range(0, len(t)-1, 1):
        maxi=maximumkivalasztas(i, t)
        seged=t[i]
        t[i]=t[maxi]
        t[maxi]=seged
    
    return t

        

def kiiras(tomb):
    for i in range(len(tomb)):
        for j in range(len(tomb[i])):
            if j+1==len(tomb[i]):
                print(tomb[i][j])
                print()
            else:
                print(tomb[i][j], end=", ")
    
def vizsgalat(regiTomb, ujTomb):
    db=0
    for i in range(len(regiTomb)):
        if regiTomb[i][0]==ujTomb[i][0] and regiTomb[i][1]==ujTomb[i][1] and regiTomb[i][2]==ujTomb[i][2]:
            db+=1
    
    return db

def main(fajl):
    t, sebesseg=feltoltes(fajl)
    # kiiras(Egyszerurendezes(t))
    # kiiras(maximumRendezes(t))
    ido=Egyszerurendezes(t.copy())
    ora=maximumRendezes(t.copy())
    print(vizsgalat(ido, ora))


main("forgalom.txt")
