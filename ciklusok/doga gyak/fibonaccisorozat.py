szam=int(input())
szam1=0
szam2=1
szam3=1
i=0
if szam!=0:
    i+=1
    if szam!=1:
        i+=1
        while szam3<=szam:
            szam3=szam1+szam2
            szam1=szam2
            szam2=szam3
            i+=1
print(i)