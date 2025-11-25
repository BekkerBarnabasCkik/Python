# kord=str(input()).split()
# kordszam=[]
# kordinatak=[]
# i=0
# for i in range(0, len(kord), 2):
#     x=int(kord[i])
#     y=int(kord[i+1])
#     kordinatak.append((x,y))
# kordinatak.append(kordinatak[0])
# print(kordinatak)

#Kordináták átalakítása 1 1 2 3 --> (1, 1) (2, 3)

# for i in range(len(x)):
#     print(x[i], y[i])
# # kordináták lejegyzése

import random
x=[0]
y=[0]
log=0
i=0
j=0
elem=0
kordinatak=[]
while log==0:
    szam=random.randint(0, 3)
    if szam==0 or szam==2:
        if szam==0:
            y.append(y[i]-1)
        else:
            y.append(y[i]+1)
        x.append(x[i])
    else:
        if szam==1:
            x.append(x[i]-1)
        else:
            x.append(x[i]+1)
        y.append(y[i])
    print(x[i], y[i])
    i+=1
    j=0
    while j<i:
        if x[j]==x[i] and y[j]==y[i]:
            log=1
            elem=j
        j+=1
print(elem)

    
for i2 in range(0, len(x), 1):
    kordinatak.append((x[i2],y[i2]))
print(kordinatak)
# kordinatak lista

for i in range(elem):
    kordinatak.pop(0)
print(kordinatak)

# # kordináták lejegyzése

jobb=0
bal=0
for i in range(len(kordinatak) -1):
    jobb+=kordinatak[i][0]*kordinatak[i+1][1]
    bal+=kordinatak[i][1]*kordinatak[i+1][0]
terulet=abs(jobb-bal)/2
print(terulet)

#Terület kiszámítása

ossz=0
for i in range(len(kordinatak)-1):
    szam1=abs(kordinatak[i][0]-kordinatak[i+1][0])
    szam2=abs(kordinatak[i][1]-kordinatak[i+1][1])
    if szam2==0 or szam1==0:
        if szam1==0:
            ossz+=szam2
        else:
            ossz+=szam1
    else: 
        if szam2<szam1:
            szam3=szam1
            szam1=szam2
            szam2=szam3
        if szam2%szam1==0:
            ossz+=szam1
        else:
            i=szam1//2
            while (i>0 and szam2%i!=0 or szam1%i!=0):
                i-=1
            ossz+=i
print(ossz)

# A határok mentén lévő egész kordináták

belso=terulet-ossz/2+1
print(belso)

# Belső egész kordináták