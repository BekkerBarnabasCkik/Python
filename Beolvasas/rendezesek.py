
def maximumRendezes(adatok):
    for i in range(len(adatok)):
        maxi=i
        for j in range(i+1, len(adatok)):
            if adatok[j][1]>adatok[maxi][1]:
                maxi=j
        
        seged=adatok[i]
        adatok[i]=adatok[maxi]
        adatok[maxi]=seged

    return adatok

def minimumKivalasztas(adatok):
    for i in range(len(adatok)):
        mini=i
        for j in range(i+1, len(adatok)):
            if adatok[j][1]<adatok[mini][1]:
                mini=j
        
        seged=adatok[i]
        adatok[i]=adatok[mini]
        adatok[mini]=seged

    return adatok

def EgyszeruCseresRendezes(adatok):
    for i in range(len(adatok)-1):
        for j in range(0, len(adatok)-1):
            if adatok[j][1]>adatok[j+1][1]:
                seged=adatok[j]
                adatok[j]=adatok[j+1]
                adatok[j+1]=seged

    return adatok

def kiiras(adatok):
    for i in range(len(adatok)):
        for j in range(len(adatok[i])):
            print(adatok[i][j], end=" ")
        print()

    
def main():
    szamok = [
    ("alma", 5),
    ("körte", 3),
    ("barack", 8),
    ("szilva", 2),
    ("cseresznye", 6),
    ("dinnye", 4),
    ("szőlő", 7),
    ("banán", 9),
    ("narancs", 1),
    ("málna", 10)
    ]
    kiiras(maximumRendezes(szamok.copy()))
    print()
    kiiras(minimumKivalasztas(szamok.copy()))
    print()
    kiiras(EgyszeruCseresRendezes(szamok.copy()))

main()
