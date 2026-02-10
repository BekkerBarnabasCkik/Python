#útlezárás
#Első sor: hány adat van, megengedett sebesség szóközzel elválasztva (1105 40)
#1000 m a lezárt szakasz
#A többi sorba: 7 21 1 60 F
#óra perc másodperc megtett_idő_másodperc melyik városból jött (Felső város, Alsó város)

#1. Mentsd le az adatokat egy tuple-s listába a tanult módon
#2. Írasd ki!
#3. Mikor ment az első autó a megfigyelt időszakbani, ami a Felső város irányába haladt
#4. Mikor ment az utolsó autó a megfigyelt időszakbani, ami az Alsó város irányába haladt
#5. Hanyadik autó haladt a leggyorsabban az adott úton
#6. Hány ilyen autó volt, aki a leggyorsabb haladt
#7. Mennyivel ment a leglasabb jármű
#8. Átlagosan mennyi idő alatt értek át az autók!

def feltoltes(adat):
    t=[]
    for i in range(adat):
        sor=input()
        adatok=sor.split(" ")
        t.append((int(adatok[0]), int(adatok[1]), int(adatok[2]), int(adatok[3]), str(adatok[4])))

    return t

def kiir(t):
    for i in range(len(t)):
        print(f"{t[i][0]}:{t[i][1]}:{t[i][2]}:{t[i][3]}:{t[i][4]}")

def varosMeghatarozas(t, varos):
    i=0
    while i<len(t) and t[i][4]!=varos:
        i+=1
    if i<len(t):
        print(F"{t[i][0]} órakor, {t[i][1]} perckor és {t[i][2]} másodperckor.")
    else:
        print("Nem volt ilyen")

def utolsoVaros(t, varos):
    i=len(t)-1
    while i>-1 and t[i][4]!=varos:
        i-=1
    if i>-1:
        print(F"{t[i][0]} órakor, {t[i][1]} perckor és {t[i][2]} másodperckor.")

def maxSebesseg(t):
    maxi=0
    db=0
    for i in range(1, len(t)):
        if t[i][3]<t[maxi][3]:
            maxi=i
        if t[i][3]==t[maxi][3]:
            db+=1
        else:
            db=0  
    
    return maxi

def minimum(t):
    mini=0
    for i in range(1, len(t)):
        if t[i][3]>t[mini][3]:
            mini=i
    
    return mini

def atlag(t):
    osszeg=0
    for i in range(len(t)):
        if t[i][3]>40:
            osszeg+=(40/60)
        else:
            osszeg+=(t[i][3]/60)
    
    return osszeg/len(t)

def mpercszamitas(t, poz):
    return ((t[poz][0]*60+t[poz][1])*60+t[poz][2])

def elozes(t):
    db=0
    leggyorsabb=t[maxSebesseg(t)][3]
    for i in range(len(t)):
        mperc=mpercszamitas(t, i)+t[i][3]
        j=i+1
        while j<len(t) and (mpercszamitas(t, j)+leggyorsabb)<mperc:
            if (mpercszamitas(t, j)+t[j][3])<mperc and t[i][4]==t[j][4]:
                db+=1
            j+=1
        
    return db

def Sorrend(t):
    i=0
    sebessegek=[]
    for i in range(len(t)):
        j=0
        while j<len(sebessegek) and sebessegek[j]<t[i][3]:
            j+=1 
        if j<len(sebessegek):
            sebessegek.insert(j, t[i][3])
        else:
            sebessegek.append(t[i][3])

    return sebessegek

def benneVan(legjobbak, ertek):
    i=0
    while i<len(legjobbak) and legjobbak[i]!=ertek:
        i+=1
    return i==len(legjobbak)

def tizLegjobb(mennyi, sebessegek):
    legjobbak=[]
    i=0
    while len(legjobbak)!=mennyi and i<len(sebessegek):
        if benneVan(legjobbak, sebessegek[len(sebessegek)-(1+i)]):
            legjobbak.append(sebessegek[len(sebessegek)-(1+i)])
        i+=1
    return legjobbak

def main():
    sor=input().split(" ")
    adat=int(sor[0])
    sebesseg=int(sor[1])
    lezartSzakasz=int(input("Lezárt szakasz: "))
    adatok=feltoltes(adat)
    kiir(adatok)
    varosMeghatarozas(adatok, "A")
    utolsoVaros(adatok, "F")
    print(f"A leggyorsabb autó a {maxSebesseg(adatok)+1}. autó volt.")
    print(f"A leglasabb autó a {3600/minimum(adatok)} km/h")
    print(f"Az átlagosan {round(atlag(adatok), 2)} perc alatt értek át az autók a lezárt szakaszon.")
    print(f"Összesen {elozes(adatok)} autó előzött.")
    sebessegek=Sorrend(adatok)
    # print(sebessegek)
    # print(tizLegjobb(10, sebessegek))

main()