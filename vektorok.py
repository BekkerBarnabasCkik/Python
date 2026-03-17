import math



def sebVektor(seb, bolintas, irany):
    vy=seb*math.sin(bolintas)
    vsik=seb*math.cos(bolintas)
    vx=vsik*math.sin(irany)
    vz=vsik*math.cos(irany)

    return [vx, vy, vz]

def vektorhossz(x, y, z):
    vektorHossz=math.sqrt(pow(x, 2)+pow(y, 2)+pow(z, 2))

def vektorOsszead(elso, masodik):
    ujx=elso[0]+masodik[0]
    ujy=elso[1]+masodik[1]
    ujz=elso[2]+masodik[2]

    return [ujx, ujy, ujz]

def vektorKivon(elso, masodik):
    ujx=elso[0]-masodik[0]
    ujy=elso[1]-masodik[1]
    ujz=elso[2]-masodik[2]

    return [ujx, ujy, ujz]

def vektorSzoroz(elso, ertek):
    ujx=elso[0]*ertek
    ujy=elso[1]*ertek
    ujz=elso[2]*ertek

    return [ujx, ujy, ujz]

def pozSzamitas(poz, velo, dt):
    vektorKivon(poz, vektorSzoroz(velo, dt))

def main():
    xyz=input()
    adatok=xyz.split(",")
    x=float(adatok[0])
    y=float(adatok[1])
    z=float(adatok[2])
    seb=float(input())
    bolintas=float(input())
    irany=float(input())
    szlsebesseg=float(input())
    szelszog=float(input())
    gravitacio=float(input())
    szelellenalas=float(input())
    fegyTorKOl=float(input())
    while seb<vektorhossz(x, y, z):
        ujpoz=pozSzamitas([x, y, z], sebVektor(seb, bolintas, irany))

#Félig kész 2.1.1-ig