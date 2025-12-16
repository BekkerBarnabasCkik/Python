f=open("be2.txt")
t=f.read()
f.close() 
ertekek=[]
hossz=0
ertek=0
for i in t:
    i=i.strip()
    if i!="":
        hossz+=1
        ertekek.append(int(i))
    else:
        hossz=0



osszes=0
max=1
szamjegyek=[]
ertek=0
for i in range(0,(len(ertekek)+1)//hossz,1):
    szamjegyek=[]
    max=i*hossz
    if max<0:
        max=0
    for j in range(12, 0, -1):
        for k in range(max, (hossz-j)+(hossz*i)+1, 1):
            if ertekek[max]<ertekek[k]:
                max=k
        szamjegyek.append(ertekek[max])
        max+=1
    for l in range(len(szamjegyek)):
        ertek+=szamjegyek[l]*(pow(10,len(szamjegyek)-(l-1)-2))
    osszes+=ertek
    ertek=0
print(osszes)

