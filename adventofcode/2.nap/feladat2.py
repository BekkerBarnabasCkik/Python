def Fajlbeolvasast(fajl):
    f=open(fajl)
    t=f.read()
    f.close()
    ertekek=[]
    for i in t:
        i=i.strip()
        ertek=(i)
        ertekek.append(ertek)
    
    return ertekek

def TömLetrahozas(tömb):
    t=[]
    ertek=""
    for i in range(len(tömb)):
        if str(tömb[i])!="-" and str(tömb[i])!=",":
            ertek+=str(tömb[i])
        else:
            t.append(str(ertek))
            ertek=""
    t.append(str(ertek))

    return t

def tTulajdonsag(m, hatar, szam):
    return m<(len(hatar)-(len(hatar)//szam)) and hatar[m]==hatar[m+(len(hatar)//szam)]

def SikerSzamlalas(hatar, siker):

    for k in range(len(hatar), 1, -1):
        if len(hatar)%(k)==0:
            siker=SikerSzamlalas2(hatar, k, siker)
    return siker

def SikerSzamlalas2(hatar, szam, siker):
    m=0
    while tTulajdonsag(m, hatar, szam):
        m+=1
    if m==(len(hatar)-(len(hatar)//szam)):
        siker+=1
    
    return siker

def Feladat(tömb):
    osszes=0
    for i in range(0, len(tömb), 2):
        for j in range(int(tömb[i]), int(tömb[i+1])+1, 1):
            j=str(j)
            siker=0
            if SikerSzamlalas(j, siker)>0:
                osszes+=int(j)
    
    return osszes

def main():
    t=TömLetrahozas(Fajlbeolvasast("be.txt"))
    print(Feladat(t))

    main()