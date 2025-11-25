import random
x=[0]
y=[0]
kordinatak=[]
alkalmak=[]
szam=0
i3=0
kori=0
for i in range(5):
    szam=random.randint(0, 3)
    lepes=random.randint(0, 20)
    if szam==0 or szam==2:
        for i3 in range(lepes):
            if szam==0:
                y.append(y[kori]-1)
            else:
                y.append(y[kori]+1)
            x.append(x[kori])
            kori+=1
    else:
        for i3 in range(lepes):
            if szam==1:
                x.append(x[kori]-1)
            else:
                x.append(x[kori]+1)
            y.append(y[kori])
            kori+=1
# kordináták lejegyzése

for i2 in range(0, len(x), 1): 
    kordinatak.append((x[i2],y[i2]))
print(kordinatak)
# kordinatak lista

maxdb=0
db=0
maxkordinata=0
tavolsag=0
legnagyobbtavolsag=0
maxhosszkor=0
for i3 in range(0,len(kordinatak), 1):
    for i4 in range(i3, len(kordinatak), 1):
        if kordinatak[i3]==kordinatak[i4]:
            db+=1
    if db>maxdb:
        maxdb=db
        maxkordinata=kordinatak[i3]
    tavolsag=(abs(0-(kordinatak[i3][0]))+abs(0-(kordinatak[i3][1])))
    if tavolsag>legnagyobbtavolsag:
        legnagyobbtavolsag=tavolsag
        maxhosszkor=kordinatak[i3]
print(maxkordinata, maxhosszkor) 

#0.10/10.10/5.10/5.-15/