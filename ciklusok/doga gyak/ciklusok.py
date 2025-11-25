szam=int(input())
i=0
for i in range(1, szam+1, 1):
    if szam==i:
        print(i)
    else:
        print(i, end=",")
print()
for i in range(szam, 0, -1):
    if i==1:
        print(i)
    else:
        print(i, end=",")
print()
while i<szam:
    print(i, end=",")
    i+=1
print(i)
print()
while i>1:
    print(i, end=",")
    i-=1
print(i)
