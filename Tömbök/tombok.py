szam=int(input())
osszes=0
db=0
for i in range(1, szam+1, 1):
    db=szam//i
    osszes+=db*i
print(osszes)

