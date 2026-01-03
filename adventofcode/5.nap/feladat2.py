def beolvasas(fajl):
    f=open(fajl)
    t=f.read()
    f.close()
    ertekek=[]
    ertek=""
    for i in t:
        i=i.strip("\n")
        if i!="" and i!="-":
            ertek+=str(i)
        elif ertek!="":
            ertekek.append(int(ertek))
            ertek="" 

    return ertekek

def VegigMenes(k, azonositok, j):
    while k<len(azonositok) and azonositok[k]!=j:
        k+=1

    return k

def feladat(ertekek):
    azonositok=[]
    db=0
    for i in range(0, len(ertekek), 2):
        for j in range(ertekek[i], ertekek[i+1]+1, 1):
            k=0
            if VegigMenes(k, azonositok, j)==len(azonositok):
                azonositok.append(j)
                db+=1
        print(ertekek[i])
    print(azonositok)
    print(db)

def main(fajl):
    ertekek=beolvasas(fajl)
    feladat(ertekek)

main("be2.txt")


#ChatGPT-vel futtatam le mert nagyon hosszú lett volna az én kódommal


    

