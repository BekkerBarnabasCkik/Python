import math

def fajlbeovlasas(fajlNev):
    f=open(fajlNev)
    t=f.read()
    f.close()
    ertekek=[]
    ertek=""
    x=[]
    y=[]
    for i in t:
        i=i.strip()
        if i!="," and i!="":
            ertek+=i
        elif i=="," and ertek!="":
            x.append(int(ertek))
            ertek=""
        elif ertek!="":
            y.append(int(ertek))
            ertek=""
    y.append(int(ertek))

    return x, y 

#Proba_5-6

def Eldontes(jox, joy, x, y):
    i=0
    # jo=True
    db=0
    while i<len(x):
        Ay=y[i]
        Ax=x[i]
        By=y[(i+1)%len(y)]
        Bx=x[(i+1)%len(x)]
        if (Ay>joy) != (By>joy) and Feltetel(jox, joy, Bx, Ax, Ay, By):
            # j=0
            # feltetel=False
            # while j<len(x) and feltetel==False:
            #     if x[j]!=joy:
            #         j+=1
            #     else:
            #         feltetel=True
            # if feltetel==True:
            # jo=True
            db+=1
        i+=1
    return (db%2)!=0

def Terulet(x, y, i, j):
    return (abs(x[i]-x[j])+1)*(abs(y[i]-y[j])+1)

def Feltetel(jox, joy, Bx, Ax, Ay, By):
    return jox<((Bx-Ax)*(joy-Ay)/(By-Ay)+Ax) and joy!=Ay and joy!=By and jox!=Ax and jox!=Bx

def Feladat(x, y):
    maxter=0
    for i in range(len(x)):
        for j in range(i+1, len(x), 1):
            jox=[x[i], x[j]]
            joy=[y[j], y[i]]
            if Eldontes(jox[0], joy[0], x, y) and Eldontes(jox[1], joy[1], x, y):
                ter=Terulet(x, y, i, j)
                # print(x[i], y[i], x[j], y[j])
                if ter>maxter:
                    maxter=ter
                    # print(maxter)

    print(maxter)



def main():
    x, y=fajlbeovlasas("proba.txt")
    Feladat(x, y)

main()