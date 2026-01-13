import random

vezetknev=str(input("Vezeték: "))
kersztnev=str(input("Kereszt: "))

def generalas(vezetknev, kersztnev):
    randomszamok=""
    for i in range(3):
        randomszamok+=str(random.randint(0, 9))
    return vezetknev+kersztnev+randomszamok+"@LTN.com"

print(generalas(vezetknev, kersztnev))

def PontokLetrehozas(pontok):
    for i in range(18*2):
        pontok.append(random.randint(0, 50))

    print(pontok)
    
    return pontok

pontok=[]

def Atlagszamlalas(pontok):
    maxi=0
    atlagok=[]
    for i in range(0, len(pontok)-1, 2):
        ertek=pontok[i]+pontok[i+1]
        if ertek%2==0:
            atlagok.append(ertek//2)
        else:
            atlagok.append((ertek)/2)
        if atlagok[len(atlagok)-1]>atlagok[maxi]:
            maxi=len(atlagok)-1

    print(atlagok)

    return maxi+1

print(Atlagszamlalas(PontokLetrehozas(pontok)))

def Fajlbeolvasas(fajl):
    f=open(fajl)
    t=f.read()
    f.close()

    vezeteknev=[]
    keresztnev=[]
    ev=[]
    pont=[]
    szamlalo=0
    ertek=""
    for i in t:
        i=i.strip()
        if i!="" and i!="/n":
            ertek+=i
        else:
            if szamlalo==0:
                vezeteknev.append(ertek)
                szamlalo+=1
                ertek=""
            elif szamlalo==1:
                keresztnev.append(ertek)
                szamlalo+=1
                ertek=""
            elif szamlalo==2:
                ev.append(int(ertek))
                szamlalo+=1
                ertek=""
            elif szamlalo==3:
                pont.append(int(ertek))
                szamlalo=0
                ertek=""
    


    return vezeteknev, keresztnev, ev, pont


ertekek=Fajlbeolvasas("nevek.txt")
vezeteknev=ertekek[0]
keresztnev=ertekek[1]
evek=ertekek[2]
pontok=ertekek[3]

ev=int(input())

def maximum(jopontok, poz):
    maxi=0
    maxpoz=0
    for i in range(1, len(jopontok), 1):
        if jopontok[i]>jopontok[maxi]:
            maxi=i
            maxpoz=poz[i]

    if len(jopontok)!=0:
        return maxpoz
    else:
        return "Nincs"
    

def Legjobb(ev, evek, pontok):
    jopontok=[]
    poz=[]
    for i in range(len(evek)-1):
        if evek[i]==ev:
            jopontok.append(pontok[i])
            poz.append(i)
    
    return maximum(jopontok, poz)



maxi=Legjobb(ev, evek, pontok)
if maxi!="Nincs":
    print(vezeteknev[maxi], keresztnev[maxi])
else:
    print("Ebben az évben nics regisztrált felhasználó")
