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
#     for i in t:
#         i=i.strip()
#         if i!="" and i!="+" and i!="*":
#             ertek+=str(i)
#         elif i=="+" or i=="*":
#             elojelek.append(i)
#         elif ertek!="":
#             szamok.append(int(ertek))
#             ertek=""
#     return szamok, elojelek, hossz

# def hosszmeghatarozas(tömb):
#     t=tömb.readline()
#     eredmenyek=[]
#     ertek=""
#     for i in t:
#         i=i.strip()
#         if i!="":
#             ertek+=str(i)
#         elif ertek!="":
#             eredmenyek.append(int(ertek))
#             ertek=""

#     return len(eredmenyek)    


# def szamokMegahatrozasa(szamok, adottoszlop, hossz):
#     joszamok=[]
#     for j in range(3):
#         joszamok.append(szamok[round(len(szamok)/hossz-adottoszlop+j*hossz)])
#     return joszamok

# def feladat(szamok, elojelek, hossz):
#     osszeredmeny=0
#     for i in range(hossz):
#         eredmeny=0
#         elojel=elojelek[i]
#         if elojel=="*":
#             eredmeny=1
#         joszamok=szamokMegahatrozasa(szamok, i, hossz)
#         maxhossz=MaxhosszuSzam(szamok)
#         osszeredmeny+=osszegSzorzat(len(szamok)//hossz, joszamok, hossz, elojel,i, eredmeny, maxhossz)

#     return osszeredmeny

# def összeadas(eredmeny, szamok, j, hossz, i):
#     eredmeny+=szamok[(j*hossz)+(i%hossz)]

#     return eredmeny

# def szorzas(eredmeny, szamok, j, hossz, i):
#     eredmeny*=szamok[(j*hossz)+(i%hossz)]

#     return eredmeny

# def MaxhosszuSzam(joszamok):
#     max=len(str(joszamok[0]))
#     for i in range(1, len(joszamok), 1):
#         if len(str(joszamok[i]))>max:
#             max=len(str(joszamok[i]))

#     return max

# def összadaasSzamok(sorokszama, szamok, maxhossz):
#     joszamok=[]
#     ertek=""
#     for i in range(sorokszama):
#         ertek=""
#         for i in range(maxhossz, 1, -1):
#             if len(str(szamok[i]))<i:
#                 ertek+=str(0)
#             else:
#                 ertek+=str(joszamok[i])
#         joszamok.append(int(ertek))

#     return joszamok   
# def osszegSzorzat(sorokszama, szamok, hossz, elojel, i, eredmeny, maxhossz):
#     print(szamok)
#     for j in range(len(szamok)):
#         if elojel=="+":  
#             print(összadaasSzamok(sorokszama, szamok ,maxhossz))
#             eredmeny=összeadas(eredmeny, szamok, j, hossz, i)
#         # else:
#         #     eredmeny=szorzas(eredmeny, szamok, j, hossz, i)

#     return eredmeny


# def main(fajl):
#     eredmenyek=Beolvasa(fajl)
#     szamok=eredmenyek[0]
#     elojelek=eredmenyek[1]
#     hossz=eredmenyek[2]

#     print(feladat(szamok, elojelek, hossz))


# main("proba.txt")

#-------------------------------------------------------------------2.próba-------------------------------------------------------------

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
    for i in t:
        i=i.strip()
        if i!="" and i!="+" and i!="*":
            ertek+=str(i)
        elif i=="+" or i=="*":
            elojelek.append(i)
        elif ertek!="":
            szamok.append(int(ertek))
            ertek=""
    return szamok, elojelek, hossz


def hosszmeghatarozas(tömb):
    t=tömb.readline()
    eredmenyek=[]
    ertek=""
    for i in t:
        i=i.strip()
        if i!="":
            ertek+=str(i)
        elif ertek!="":
            eredmenyek.append(int(ertek))
            ertek=""

    return len(eredmenyek)

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

def SzamMeghatarozas(alapszamok, hossz, oszlop, elojelek):
    összeredmeny=0
    joszamok=[]
    for i in range(len(alapszamok)//hossz):
        joszamok.append(str(alapszamok[round(len(alapszamok)/hossz-oszlop+i*hossz)]))
    max=maximum(joszamok)
    ertek=""
    ertekek=[]
    if elojelek[len(elojelek)-1-oszlop]=="+":
        for i in range(max):
            for j in range(len(joszamok)):
                if len(joszamok[j])>i:
                    ertek+=str(joszamok[j][i])
            ertekek.append(int(ertek))
            ertek=""
        összeredmeny+=összeadas(ertekek)
    else:
        for i in range(max):
            for j in range(len(joszamok)):
                if len(joszamok[j])>i:
                    ertek+=str(joszamok[j][len(joszamok[j])-1-i])
            ertekek.append(int(ertek))
            ertek=""
        összeredmeny+=szorzas(ertekek)
    print("ertek")
    print(ertekek)
    #Az összadásos számokat írja ki de jól

    return összeredmeny

def maximum(joszamok):
    max=len(str(joszamok[0]))
    for i in range(1, len(joszamok), 1):
        if len(str(joszamok[i]))>max:
            max=len(str(joszamok[i]))

    return max



def Feladat(alapszamok, hossz, elojelek):
    összeredmeny=0
    for i in range(hossz):
        összeredmeny+=SzamMeghatarozas(alapszamok, hossz, i, elojelek)

    return összeredmeny

def main(fajl):
    eredmenyek=Beolvasa(fajl)
    szamok=eredmenyek[0]
    elojelek=eredmenyek[1]
    hossz=eredmenyek[2]

    print(Feladat(szamok, hossz, elojelek))

main("be.txt")





# def szamokMegahatrozasa(szamok, adottoszlop, hossz):
#     joszamok=[]
#     for j in range(3):
#         joszamok.append(szamok[round(len(szamok)/hossz-adottoszlop+j*hossz)])
#     return joszamok


# def main(fajl):
#     eredmenyek=Beolvasa(fajl)
#     szamok=eredmenyek[0]
#     elojelek=eredmenyek[1]
#     hossz=eredmenyek[2]

#     print(feladat(szamok, elojelek, hossz))


# main("proba.txt")