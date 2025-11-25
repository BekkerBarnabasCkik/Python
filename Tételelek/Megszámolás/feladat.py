import random
szam=int(input())
t=[]
for i in range(0, szam, 1):
    t.append(random.randint(1, 6))
db=0
for i in range(0, len(t), 1):
    if t[i]==6:
        db+=1
print(len(t)-db, t)