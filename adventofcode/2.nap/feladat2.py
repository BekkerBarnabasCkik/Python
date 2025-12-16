def fajlbeolvasas(fajl):
    f=open(fajl)
    t=f.read()
    f.close()
    ertekek=[]
    for i in t:
        i=i.strip()
        ertek=(i)
        ertekek.append(ertek)
    return(ertekek)

def tTulajdonsag(tomb, i):
    return str(tomb[i])!="-" and str(tomb[i])!=","

def tombletrehozas(ertekek):
    t=[]
    ertek=""
    for i in range(len(ertekek)):
        if tTulajdonsag(ertekek, i):
            ertek+=str(ertekek[i])
        else:
            t.append(str(ertek))
            ertek=""
    t.append(str(ertek))
    return t


# def tombolKivagunkEgyDarabot(tomb, mennyit, honnan):
#     mit csinál

#     return darabTomb

# def egyezoe()
    
#     return true
def sikerTulajdonasag(m, elemhossza, darabolasSzam):
    return m<(len(elemhossza)-(len(elemhossza)//darabolasSzam)) and elemhossza[m]==elemhossza[m+(len(elemhossza)//darabolasSzam)]

def sikerekSzama(elemhossza, darabolasSzam):
    m=0
    while sikerTulajdonasag(m, ):
        #
        m+=1
    if m==(len(elemhossza)-(len(elemhossza)//darabolasSzam)):
        siker+=1

def sikerVizsgálat(elemhossza):
    siker=0
    for k in range(len(elemhossza), 1, -1):
        if len(elemhossza)%(k)==0:
            sikerekSzama(elemhossza, k)
    if siker>0:
        osszes+=int(elemhossza)
    return(osszes)

def feladat(tömb, i):
    osszes=0
    for i in range(0, len(tömb), 2):
        for j in range(int(tömb[i]), int(tömb[i+1])+1, 1):
            j=str(j)
            sikerVizsgálat(j)
    return(osszes)

def main():
    t=tombletrehozas(fajlbeolvasas("be.txt"))
    feladat(t)