import random
szam=int(input())
t=[]
i=0
for i in range(szam):
    t.append(random.randint(1, 100))
while i<len(t) and t[i]!=67:
    i+=1
if i<szam:
    print("Van")
else:
    print("Nincs")
