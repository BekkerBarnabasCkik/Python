szam=input()
szamok=szam.split()
szam1=int(szamok[0])
szam2=int(szamok[1])
if szam2<szam1:
    szam3=szam1
    szam1=szam2
    szam2=szam3
if szam2%szam1==0:
    print(szam1)
else:
    i=szam1//2
    while (i>0 and szam2%i!=0 or szam1%i!=0):
        i-=1
    print(f"A legnagyobb közös osztó: {i}")

legnagyobb=szam2
while legnagyobb%szam1!=0 or legnagyobb%szam2!=0:
    legnagyobb+=1
print(legnagyobb)