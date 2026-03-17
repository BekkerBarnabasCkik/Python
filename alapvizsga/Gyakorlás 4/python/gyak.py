def bekeres():
    meter=str(input("Méter: "))
    deci=str(input("Deciméter: "))
    centi=str(input("Centiméter: "))

    return meter, deci, centi

def Vizsgal(centi, deci, meter):
    if centi<10 and deci<10:
        print(f"{meter}:{deci}:{centi}")
    else:
        print(f"Nem megfelelő bemenet.")

def centimeterben(meter, decimeter, centimeter):
    return meter*100+decimeter*10+centimeter

def sztringben(centimeter):
    print(centimeter)
    meter=centimeter//100
    decimeter=(centimeter-meter*100)//10
    centimeter=centimeter%10
    ertek=str(meter)+":"+str(decimeter)+":"+str(centimeter)
    return ertek

def fajlbeolvasas(fajl):
    f=open(fajl, "r", encoding="utf-8")
    t=f.readlines()
    f.close()
    adatok=[]
    for i in t:
        i=i.strip().split(";")
        adatok.append((int(i[0]), str(i[1]), str(i[2]), int(i[3]), int(i[4]), int(i[5])))

    return adatok
def gyoztes(adatok):
    maxi=0
    maxcm=0
    for i in range(len(adatok)):
        cm=centimeterben(adatok[i][3], adatok[i][4], adatok[i][5])
        if cm>maxcm:
            maxi=i
            maxcm=cm
    
    return maxi

def atlagszamitas(mit, adatok):
    ido=0
    db=0
    for i in range(len(adatok)):
        if adatok[i][2]==mit:
            ido+=adatok[i][3]*100+adatok[i][4]*10+adatok[i][5]
            db+=1
    
    return round(ido/db)

def kereses(adatok):
    for i in range(len(adatok)):
        nev=adatok[i][1]
        if nev[len(nev)-5:len(nev)]=="Lajos":
            print(adatok[i])

def main(fajl):
    meter, deci, centi=bekeres()
    Vizsgal(int(centi), int(deci), int(meter))
    meter=int(input())
    deci=int(input())
    centi=int(input())
    print(sztringben(centimeterben(meter, deci, centi)))
    adatok=fajlbeolvasas(fajl)
    print(adatok[gyoztes(adatok)])
    sztringben((atlagszamitas("CVSE", adatok)))
    kereses(adatok)
main("csigalimpia.txt")