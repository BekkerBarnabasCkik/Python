#állatkerti ételbeszállítás

# 40
# 5 19 Ablak Antal -
# 1 120 Alma Dalma GYEP

#körzet, szavazat, vezeték név, keresztnév, párt
#1. tároljuk le az adatoakt
def letarolas(hossz):
    t=[]
    for i in range(hossz):
        sor=input().split(" ")
        t.append((int(sor[0]), int(sor[1]), str(sor[2]), str(sor[3]), str(sor[4])))
    
    return t

#2. írju ki
def kiiras(adatok):
    for i in range(len(adatok)):
        print(adatok[0], adatok[1], adatok[2], adatok[3], adatok[4])


#3. határozd meg, hogy az egyes párt hány szavazatot kapott!
def partokmeghatarozasa(adatok):
    partok=[]
    for i in range(len(adatok)):
        j=0
        while j<len(partok) and partok[j]!=adatok[i][4]:
            j+=1
        if j==len(partok):
            partok.append(adatok[i][4])
    
    return partok

def szavazatszamok(adatok):
    partok=partokmeghatarozasa(adatok)
    szavazatok-
    for i in range(len(partok)):
        for j in range(len(adatok)):
            if adatok[j][4]==partok[i]:
                db+=adatok[i][1]
        szavazatok.append(db)


#4. Melyik párt kapta a legtöbb szavazatot?


#5. Nyert-e valamelyik kerületben a függetlenek pártja: -
#6. Megadunk egy nevet, nézzük meg, hogy indult-e valamelyik kerületben,
#ha indul, hol?
#7. Ki kapta a legtöbb szavazatot?
#8. Átlagosan az egyes képviselők hány szavazatot kaptak?

def main():
    hossz=int(input())
    adatok=letarolas(hossz)
    kiiras(adatok)