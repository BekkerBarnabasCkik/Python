#Be szam, hossz
import random
szam=int(input())
t=[]
osszeg=0
for i in range(0, szam, 1):
    t.append(random.randint(1, 6))
    osszeg+=t[i]
print(round(osszeg/len(t), 2), t)

