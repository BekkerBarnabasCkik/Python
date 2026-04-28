import random

def Jatekter(N, M, Ndb, Mdb, szamok, SzamokTelj):
    if Ndb!=N:
        szamok.append(random.randint(0, 9))
        print(szamok[len(szamok)-1], end=" ")
        Jatekter(N, M, Ndb+1, Mdb, szamok, SzamokTelj)
    elif Mdb!=M:
        SzamokTelj.append((szamok))
        szamok=[]
        Ndb=0
        print()
        Jatekter(N, M, 0, Mdb+1, szamok, SzamokTelj)

    return SzamokTelj

def Becsapodas(szamok, N, M, Ndb, Mdb, legnagyobb, pozok):
    if Ndb!=N:
        if len(pozok)!=0:
            if szamok[0][Mdb*N+Ndb]>legnagyobb:
                legnagyobb=szamok[0][Mdb*N+Ndb]
                pozok=[Ndb]
            elif szamok[0][Mdb*N+Ndb]==legnagyobb:
                pozok.append(Ndb)
        else:
            pozok.append(Ndb)
            legnagyobb=szamok[0][Mdb*N+Ndb]
        pozok=Becsapodas(szamok, N, M, Ndb+1, Mdb, legnagyobb, pozok)
    
    return pozok 

def vizsgalat(adatok, sorElem, Oszlop, legnagyobbak, vizsgalandoHelyek):
    viszagalandoPozok=[(0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    if Oszlop<len(adatok):
        legnagyobbak=LegnagyobbKivalasztas(adatok, 0, 0, legnagyobbak, vizsgalandoHelyek ,viszagalandoPozok, 0)
    else:
        return legnagyobbak


def AktualisElemErteke(adatok, oszlop, VizsgalandoPozok, sorElem, n):
    return adatok[oszlop+VizsgalandoPozok[n][1]][sorElem+VizsgalandoPozok[n][1]]

def HozzaFuzes(legnagyobbak, n):
    if n<len(legnagyobbak):
        joLegnagyobb=HozzaFuzes(legnagyobbak, n+1)
        joLegnagyobb.append(legnagyobbak[n])
    else:
        return joLegnagyobb

def LegnagyobbKivalasztas(adatok, sorElem, oszlop, legnagyobbak, VizsgalandoHelyek, VizsgalandoPozok, n):
    if sorElem<len(VizsgalandoHelyek):
        if n<len(VizsgalandoPozok):
            if len(legnagyobbak)>0:
                if AktualisElemErteke(adatok, oszlop, VizsgalandoPozok, sorElem, n)>legnagyobbak[0]:
                    legnagyobbak=AktualisElemErteke(adatok, oszlop, VizsgalandoPozok, sorElem, n)
                elif AktualisElemErteke(adatok, oszlop, VizsgalandoPozok, sorElem, n)==legnagyobbak[0]:
                    legnagyobbak.append(AktualisElemErteke(adatok, oszlop, VizsgalandoPozok, sorElem, n))
            else:
                legnagyobbak.append(AktualisElemErteke(adatok, oszlop, VizsgalandoPozok, sorElem, n))
        else:
            joLegnagyobbak=HozzaFuzes(legnagyobbak, 0)
    else:
        return legnagyobbak


def main():
    n=int(input())
    m=int(input())
    szamok=Jatekter(n, m, 0, 0, [], [])
    print()
    pozok=Becsapodas(szamok, n, m, 0, 0, 0, [])
    print(pozok)
    print(szamok)
    print(vizsgalat(szamok, 0, 0, [], pozok))



main()

