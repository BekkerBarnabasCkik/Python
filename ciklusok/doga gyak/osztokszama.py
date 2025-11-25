import math
szam=int(input())
osztok=2
if szam==1:
    print(1)
else:
    for i in range(2, szam//2+1, 1):
        if szam%i==0:
            osztok+=1
    print(osztok)