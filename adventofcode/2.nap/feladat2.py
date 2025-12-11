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

osszes=0
for i in range(0, len(t), 2):
    for j in range(int(t[i]), int(t[i+1])+1, 1):
        ertek=str(j)
        for k in range(2, len(ertek)+1, 1):
            # szamjegyek=[]
            if len(ertek)%(k)==0:
                # for l in range(len(ertek)):
                #     szamjegyek.append(ertek[l])
                m=0
                while m<len(ertek)-1 and ertek[m]==ertek[(m+(round(len(ertek)/(k))))]:
                    m+=1
                if m==len(ertek)-1:
                    szam=""
                    for n in range(len(ertek)):
                        szam+=str(ertek[n])
                    osszes+=int(szam)
                    print(szam, osszes)
                    
print(osszes)