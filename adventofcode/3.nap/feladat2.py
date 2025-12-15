f=open("proba.txt")
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
max=0
maxuj=0
for i in range(0,len(ertekek)//hossz,1):
    for j in range(11,1,-1):
        maxuj=max+1
        for k in range(max+1, hossz-j, 1):
            if ertekek[maxuj]<ertekek[k]:
                maxuj=k
        max=maxuj
        print(ertekek[maxuj])
