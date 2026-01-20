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

def tavolsag(x, y, i, j):
    return (abs(x[j]-x[i])+1)*(abs(y[j]-y[i])+1)

def Kivalasztas(x, y):
    maxter=0
    for i in range(len(x)-1):
        for j in range(i+1, len(x), 1):
            ter=tavolsag(x, y, i, j)
            if ter>maxter:
                maxter=ter
                print(maxter)
    print(maxter)



ertekek=fajlbeovlasas("be.txt")
x=ertekek[0]
y=ertekek[1]
Kivalasztas(x, y)


# def eldonters(x1, x2, y1, y2):
#     while 

