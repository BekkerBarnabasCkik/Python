szam=int(input())
for i in range(szam):
    for i2 in range(i+1):
        print("*", end=" ")
    print()

print()
for i in range(szam):
    for i2 in range(szam-i-1):
        print(" ", end="")
    for i2 in range(i+1):
        print("*", end=" ")
    print()
