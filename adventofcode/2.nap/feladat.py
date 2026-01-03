
def fajlbeovlasas(fajlNev):
    f=open(fajlNev)
    t=f.read()
    f.close()
    ertekek=[]
    for i in t:
        i=i.strip()
        ertek=(i)
        ertekek.append(ertek)
    return ertekek

def tTulajdonsag(ertekek, i):
    return str(ertekek[i])!="-" and str(ertekek[i])!=","

def intervallumMeghatarozas(ertekek):
    t=[]
    ertek=""
    for i in range(len(ertekek)):
        if tTulajdonsag(ertekek,i):
            ertek+=str(ertekek[i])
        else:
            t.append(str(ertek))
            ertek=""
    t.append(str(ertek))
    return t

def darabolas(ertek, mettol, meddig):
    return ertek[mettol:meddig]

def tTulajdonsagEgyezo(ertek):
    return len(ertek)%2==0 and ertek[:round(len(ertek)/2)]==ertek[round(len(ertek)/2):]

def intervallumOsszead(mettol,meddig):
    ossz=0
    for j in range(mettol, meddig, 1):
        ertek=str(j)
        if tTulajdonsagEgyezo(ertek):
            ossz+=int(ertek)
    return ossz

def feladat(t):
    ossz=0
    for i in range(0, len(t), 2):
        ossz+=intervallumOsszead(int(t[i]),int(t[i+1])+1)
    return ossz
            
# ertek="1534"
# hossz=round(len(ertek)/2)
# print(hossz)
# print(ertek[:hossz])

def main():
    t=intervallumMeghatarozas(fajlbeovlasas("be.txt"))
    print(feladat(t))

main()