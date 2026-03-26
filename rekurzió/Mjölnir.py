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

def main():
    n=int(input())
    m=int(input())
    szamok=Jatekter(n, m, 0, 0, [], [])
    print()
    pozok=Becsapodas(szamok, n, m, 0, 0, 0, [])
    print(pozok)


main()

