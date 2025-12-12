f=open("proba.txt")
t=f.read()
f.close()
ertekek=[]
for i in t:
    i=i.strip()
    ertek=(i)
    ertekek.append(ertek)
t=[]
ertek=""
for i in range(len(ertekek)):
    if str(ertekek[i])!="-" and str(ertekek[i])!=",":
        ertek+=str(ertekek[i])
    else:
        t.append(str(ertek))
        ertek=""
t.append(str(ertek))
print(t)

ossz=0
for i in range(0, len(t), 2):
    for j in range(int(t[i]), int(t[i+1])+1, 1):
        ertek=str(j)
        if len(ertek)%2==0:
            if ertek[:round(len(ertek)/2)]==ertek[round(len(ertek)/2):]:
                print(ertek)
                ossz+=int(ertek)
print(ossz)
            
# ertek="1534"
# hossz=round(len(ertek)/2)
# print(hossz)
# print(ertek[:hossz])