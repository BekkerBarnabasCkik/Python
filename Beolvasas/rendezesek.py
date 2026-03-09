szamok=[0, 3, -5, 10, 2, 900, -15]

def maximumRendezes(adatok):
    for i in range(len(adatok)):
        maxi=i
        for j in range(i+1, len(adatok)):
            if adatok[j]>adatok[maxi]:
                maxi=j
        
        seged=adatok[i]
        adatok[i]=adatok[maxi]
        adatok[maxi]=seged

    return adatok

def minimumKivalasztas(adatok):
    for i in range(len(adatok)):
        mini=i
        for j in range(i+1, len(adatok)):
            if adatok[j]<adatok[mini]:
                mini=j
        
        seged=adatok[i]
        adatok[i]=adatok[mini]
        adatok[mini]=seged

    return adatok

def EgyszeruCseresRendezes(adatok):
    for i in range(len(adatok)-1):
        for j in range(0, len(adatok)-1):
            if adatok[j]>adatok[j+1]:
                seged=adatok[j]
                adatok[j]=adatok[j+1]
                adatok[j+1]=seged

    return adatok

def main():
    print(maximumRendezes(szamok.copy()))
    print(minimumKivalasztas(szamok.copy()))
    print(EgyszeruCseresRendezes(szamok.copy()))

main()
