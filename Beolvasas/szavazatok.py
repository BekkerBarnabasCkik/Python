#állatkerti ételbeszállítás

# 40
# 5 19 Ablak Antal -
# 1 120 Alma Dalma GYEP
#...
#körzet, szavazat, vezeték név, keresztnév, párt
#1. tároljuk le az adatoakt
#2. írju ki
#3. határozd meg, hogy az egyes párt hány szavazatot kapott!
#4. Melyik párt kapta a legtöbb szavazatot?
#5. Nyert-e valamelyik kerületben a függetlenek pártja: -
#6. Megadunk egy nevet, nézzük meg, hogy indult-e valamelyik kerületben,
#ha indul, hol?
#7. Ki kapta a legtöbb szavazatot?
#8. Átlagosan az egyes képviselők hány szavazatot kaptak?


def Beolvasas(fajl):
    f=open(fajl, "r", encoding="utf-8")
    adatok=f.readlines()
    f.close()
    t=[]
    hossz=adatok[0].split()
    for i in range(1,len(adatok), 1):
        adottsor=adatok[i].split()
        t.append((int(adottsor[0]), int(adottsor[1]), str(adottsor[2]), str(adottsor[3]), str(adottsor[4])))
    
    return t

def maximumkivalasztas(t, i):
    maxi=i
    for j in range(i, len(t), 1):
        if t[j][4]>t[maxi][4]:
            maxi=j
    
    return maxi

def növekvőSorrend(tömb):
    for i in range(len(tömb)-1):
        maxi=maximumkivalasztas(tömb, i)
        seged=tömb[i]
        tömb[i]=tömb[maxi]
        tömb[maxi]=seged
    
    return tömb

def kiiras(tomb):
    for i in range(len(tomb)):
        for j in range(len(tomb[i])):
            if j+1==len(tomb[i]):
                print(tomb[i][j])
                print()
            else:
                print(tomb[i][j], end=", ")


def legtobbjelolt(t):
    db=0
    maxDB=0
    maxPart=""
    for i in range(0, len(t)-1, 1):
        if t[i][4]==t[i+1][4]:
            db+=1
        else:
            if db>maxDB:
                maxDB=db
                maxPart=t[i][4]
                db=0
            db=0    
    return maxPart

def main(fajl):
    adatok=növekvőSorrend(Beolvasas(fajl))
    kiiras(adatok)
    print(legtobbjelolt(adatok))


main("szavazatok.txt")