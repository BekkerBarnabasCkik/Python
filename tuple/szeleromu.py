def Feltoltes(darab):
    t=[]
    for i in range(darab):
        sor=input()
        adatok=sor.split(";")
        t.append((adatok[0], adatok[1], adatok[2], int(adatok[3]), int(adatok[4]), int(adatok[5])))
    
    return t

def kiiras(tomb):
    for i in range(len(tomb)):
        for j in range(len(tomb[i])):
            if j+1==len(tomb[i]):
                print(tomb[i][j])
                print()
            else:
                print(tomb[i][j], end=", ")

def Megszamolas(tombok):
    osszes=0
    for i in range(len(tombok)):
        darab=tombok[i][3]
        osszes+=darab
    
    return osszes

def maximum(t):
    maxi=0
    maxdb=t[0][3]
    for i in range(1, len(t), 1):
        db=t[i][3]
        if db>maxdb:
            maxi=i
            maxdb=t[i][3]

    return maxi

def ev_megyeMeghatarozas(t, mit):
    evek_megye=[]
    for i in range(len(t)):
        ev=t[i][mit]
        j=0
        while j<len(evek_megye) and evek_megye[j]!=ev:
            j+=1
        if j==len(evek_megye):
            evek_megye.append(ev)

    return evek_megye

def EvMegszamolas(evek, tomb):
    darabok=[]
    maxi=0
    for i in range(len(evek)):
        ev=evek[i]
        osszes=0
        for j in range(len(tomb)):
            ujev=tomb[j][5]
            if ujev==ev:
                db=tomb[j][3]
                osszes+=db
        darabok.append(osszes)
    print(darabok)
    print(evek)
    return darabok

def maximumkivalasztas(darabok):
    maxi=0
    for i in range(1, len(darabok), 1):
        if darabok[i]>darabok[maxi]:
            maxi=i
    
    return maxi

def leghozsabbmegye(megyek):
    maxi=0
    for i in range(len(megyek)):
        if len(megyek[i])>len(megyek[maxi]):
            maxi=i
    
    return len(megyek[maxi])

def megyeKiiras(megye, leghoszabb):
    print(megye, end="")
    for i in range(leghoszabb-len(megye)):
        print(" ", end="")



def megyekMegszamolas(megyek, evek, t):
    maxhossz=leghozsabbmegye(megyek)
    for i in range(len(megyek)):
        megyeKiiras(megyek[i], maxhossz)
        for j in range(len(evek)):
            db=kereses_szamlalas(megyek[i], evek[j], t)
            if db>0:
                print(db, end=" ")
            else:
                print(" ", end=" ")
        print()

def kereses_szamlalas(jomegye, joev, t):
    osszes=0
    for i in range(len(t)):
        _,megye,_,db,_,ev=t[i]
        if megye==jomegye and ev==joev:
            osszes+=db
    
    return osszes


def main():
    n=int(input())
    t=Feltoltes(n)
    kiiras(t)
    print(Megszamolas(t))
    maxi=maximum(t)
    tel,_,_,_,_,ev=t[maxi]
    print(tel, ev)
    evek=ev_megyeMeghatarozas(t, 5)
    maxev=maximumkivalasztas(EvMegszamolas(evek, t))
    joev=evek[maxev]
    print(joev)

    megyek=ev_megyeMeghatarozas(t, 1)
    print(megyek)
    megyekMegszamolas(megyek, evek, t)
main()