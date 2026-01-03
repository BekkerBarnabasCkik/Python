def SzetszedFajlbol(fajl):
    f=open(fajl)
    t=f.read()
    f.close()
    hatarok=[]
    szamok=[]
    ertek=""
    atvaltas=0
    for i in t:
        i=i.strip()
        if i!="-" and i!="":
            ertek+=str(i)
        elif ertek=="":
            atvaltas=1
        else:
            if atvaltas==0:
                hatarok.append(int(ertek))
            else:
                szamok.append(int(ertek))
            ertek=""
    szamok.append(int(ertek))        
    return hatarok, szamok


def feladat(hatarok, ertekek):
    db=0
    for i in range(len(ertekek)):
        ertek=ertekek[i]
        j=1
        while (j<len(hatarok)-2) and (ertek<hatarok[j-1] or ertek>hatarok[j]):
            j+=2
        if j+1<len(hatarok):
            db+=1
    return db


def main(fajl):
    eredmenyek=SzetszedFajlbol(fajl)
    hatarok=eredmenyek[0]
    ertekek=eredmenyek[1]
    print(hatarok)
    print(ertekek)
    print(feladat(hatarok, ertekek))

main("be1.txt")


    

