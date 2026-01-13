def Beolvasa(fajl):
    f=open(fajl)
    f2=open(fajl)
    hossz=hosszmeghatarozas(f2)
    t=f.read()
    f.close()
    f2.close()
    elojelek=[]
    szamok=[]
    ertek=""
    for i in range(len(t)):
        i=t[i].strip()
        if i=="+" or i=="*":
            elojelek.append(i)
        else:
            szamok.append(i)
    return szamok, elojelek, hossz

def hosszmeghatarozas(tömb):
    t=tömb.readline()
    eredmenyek=[]
    ertek=""
    for i in t:
        i=i.strip()
        eredmenyek.append(i)


    return len(eredmenyek)-1


def main(fajl):
    eredmenyek=Beolvasa(fajl)
    szamok=eredmenyek[0]
    elojelek=eredmenyek[1]
    hossz=eredmenyek[2]

    print(Feladat(szamok, hossz, elojelek))

def TeljesÖsszegMeghatarozas(hossz, alapszamok, elojelek, összeredmeny):
    joszamok=[]
    for i in range(hossz+1):
        ertek=SzamMeghatarozas(alapszamok, hossz, i, elojelek)
        if ertek!=None:
            joszamok.append(ertek)
        else:
            összeredmeny+=összegMeghatarozas(elojelek[0], joszamok)
            joszamok=[]
            elojelek.pop(0)
    
    return elojelek, összeredmeny

def Feladat(alapszamok, hossz, elojelek):
    összeredmeny=0
    ertekek=TeljesÖsszegMeghatarozas(hossz, alapszamok, elojelek, összeredmeny)
    elojelek=ertekek[0]

    return ertekek[1]

def összegMeghatarozas(elojel, ertekek):
    if elojel=="+":
        return összeadas(ertekek)
    else:
        return szorzas(ertekek)
    
def összeadas(szamok):
    eredmeny=0
    for i in range(len(szamok)):
        eredmeny+=szamok[i]

    return eredmeny

def szorzas(szamok):
    eredmeny=1
    for i in range(len(szamok)):
        eredmeny*=szamok[i]

    return eredmeny

def szures(szamok):
    ertek=""
    for i in range(len(szamok)):
        if szamok[i]!="" and szamok[i]!=",":
            ertek+=szamok[i]
    if ertek!="":
        return ertek
    
def SzamMeghatarozas(alapszamok, hossz, oszlop, elojelek):
    joszamok=[]
    joszamok=alapJoszam(alapszamok, hossz, joszamok, oszlop)
    ertek=szures(joszamok)
    if ertek!=None:
        return int(ertek)
    


def alapJoszam(alapszamok, hossz, joszamok, oszlop):
    for i in range(4):
        if i>0:
            joszamok.append(alapszamok[i*hossz+oszlop+i])
        else:
            joszamok.append(alapszamok[i*hossz+oszlop])

    return joszamok


main("be.txt")


# def Beolvasa(fajl):
#     f=open(fajl)
#     f2=open(fajl)
#     hossz=hosszmeghatarozas(f2)
#     t=f.read()
#     f.close()
#     f2.close()
#     elojelek=[]
#     szamok=[]
#     ertek=""
#     for i in range(len(t)):
#         i=t[i].strip()
#         if i=="+" or i=="*":
#             elojelek.append(i)
#         else:
#             szamok.append(i)
#     return szamok, elojelek, hossz

# def hosszmeghatarozas(tömb):
#     t=tömb.readline()
#     eredmenyek=[]
#     ertek=""
#     for i in t:
#         i=i.strip()
#         eredmenyek.append(i)


#     return len(eredmenyek)-1


# def main(fajl):
#     eredmenyek=Beolvasa(fajl)
#     szamok=eredmenyek[0]
#     elojelek=eredmenyek[1]
#     hossz=eredmenyek[2]

#     print(Feladat(szamok, hossz, elojelek))



# def Feladat(alapszamok, hossz, elojelek):
#     összeredmeny=0
#     joszamok=[]
#     for i in range(hossz+1):
#         ertek=SzamMeghatarozas(alapszamok, hossz, i, elojelek)
#         if ertek!=None:
#             joszamok.append(ertek)
#         else:
#             print(joszamok)
#             összeredmeny+=összegMeghatarozas(elojelek[0], joszamok)
#             joszamok=[]
#             elojelek.pop(0)
#     return összeredmeny

# def összegMeghatarozas(elojel, ertekek):
#     if elojel=="+":
#         return összeadas(ertekek)
#     else:
#         return szorzas(ertekek)
    
# def összeadas(szamok):
#     eredmeny=0
#     for i in range(len(szamok)):
#         eredmeny+=szamok[i]

#     return eredmeny

# def szorzas(szamok):
#     eredmeny=1
#     for i in range(len(szamok)):
#         eredmeny*=szamok[i]

#     return eredmeny

# def szures(szamok):
#     ertek=""
#     for i in range(len(szamok)):
#         if szamok[i]!="" and szamok[i]!=",":
#             ertek+=szamok[i]
#     if ertek!="":
#         return ertek
    
# def SzamMeghatarozas(alapszamok, hossz, oszlop, elojelek):
#     joszamok=[]
#     joszamok=alapJoszam(alapszamok, hossz, joszamok, oszlop)
#     ertek=szures(joszamok)
#     if ertek!=None:
#         return int(ertek)
    


# def alapJoszam(alapszamok, hossz, joszamok, oszlop):
#     for i in range(4):
#         if i>0:
#             joszamok.append(alapszamok[i*hossz+oszlop+i])
#         else:
#             joszamok.append(alapszamok[i*hossz+oszlop])

#     return joszamok


# main("be.txt")