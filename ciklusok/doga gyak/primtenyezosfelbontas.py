szam=int(input())
if szam==0 or szam==1:
    print(szam)
else:
    while szam%2==0:
        if szam/2==1:
            print(2)
        else:
            print(2, end="*")
        szam/=2
    i=3
    while i<=szam:
        if szam%i==0:
            if szam/i==1:
                print(i)
            else:
                print(i, end="*")
            szam/=i
        else:
            i+=2