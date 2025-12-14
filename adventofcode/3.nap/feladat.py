f=open("be.txt")
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
for i in range(0, len(ertekek), 1):
    tizes=ertekek[i]*10
    if (i+1)%hossz!=0:
        for j in range(i+1,((i+1)//hossz+1)*hossz,1):
            ertek=tizes+ertekek[j]
            if ertek>max:
                max=tizes+ertekek[j]
    else:
        osszes+=max
        max=0
print(osszes)