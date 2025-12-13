f=open("be2.txt")
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


# def tombolKivagunkEgyDarabot(tomb, mennyit, honnan):
#     mit csinál

#     return darabTomb

# def egyezoe()
    
#     return true


osszes=0
for i in range(0, len(t), 2):
    for j in range(int(t[i]), int(t[i+1])+1, 1):
        j=str(j)
        siker=0
        for k in range(len(j), 1, -1):
            if len(j)%(k)==0:
                m=0
                while m<(len(j)-(len(j)//k)) and j[m]==j[m+(len(j)//k)]:
                    m+=1
                if m==(len(j)-(len(j)//k)):
                    siker+=1
        if siker>0:
            osszes+=int(j)
print(osszes)