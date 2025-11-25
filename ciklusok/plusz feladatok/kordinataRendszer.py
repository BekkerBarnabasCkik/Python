import random
x=[0]
y=[0]
kordinatak=[]
alkalmak=[]
szam=0
i3=0
for i in range(10):
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
    
    

#maxdb=0
#maxkoordináta=semmi
# végigmész az elejétől
#   végimész az adott számtól
#       megszámolod ha egyező a koordináta
#   eldöntöd, hogy nagoybb-e a megjelölt értéktől
        # ha nagyobb lemented
#kiírod a maxkoordinátát
    

# t=[]
# t.append((x,y))
# # x,y=(x,y)

#manhattan tavolsag: y=|𝑥1 −𝑥2|+|𝑦1 −𝑦2| 
