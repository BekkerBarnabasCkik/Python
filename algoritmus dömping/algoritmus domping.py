#-------------Tömb létrehozása-------------
import random
n=int(input())
t=[]
for i in range(n):
    t.append((random.randint(1, 100)))
for i in range(0, n, 1):
    if i==n-1:
        print(t[i])
    else:
        print(t[i], end=", ")

#-------------2.Feladat----------------
maxi=0
for i in range(1, n, 1):
    if t[i]>t[maxi]:
        maxi=i
if t[maxi]<=90:
    print(f"{maxi}, Igen")
else:
    print(f"{maxi}, Nem")
#------------3.Feladat--------------
for i in range(len(t)-2, 0, -1):
    szam=0
    while szam!=i:
        if t[i]>t[szam]:
            if t[i]>90:
                t[i]-=(t[i]-90)
            t.insert(szam, t[i])
            t.pop(i+1)
        else:
            szam+=1
for i in range(0, n, 1):
    if i==n-1:
        print(t[i])
    else:
        print(t[i], end=", ")
    
#----------4.Feladat-------------
for i in range(len(t)-1, -1, -1):
    if i==0:
        print(t[i])
    else:
        print(t[i], end=", ")
#----------5.Feladat-------------
for i in range(len(t)-1, 0, -1):
    szam=0
    if t[i]<t[szam]:
        while szam!=i:
            if t[i]<t[szam]:
                t.insert(szam, t[i])
                t.pop(i+1)
            else:
                szam+=1
for i in range(0, len(t), 1):
    if i==len(t)-1:
        print(t[i])
    else:
        print(t[i], end=", ")
#-------6.Feladat--------------
alkalom=1
for i in range(2, n-2+1, 1):
    alkalom*=i
print(f"{round(((n-2)*2-1)*11.23, 2)}")
print(alkalom)