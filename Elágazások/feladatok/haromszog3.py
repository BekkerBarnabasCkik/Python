o1=float(input())
o2=float(input())
o3=float(input())

if o1+o2>o3 and o1+o3>o2 and o2+o3>o1:
    if o1==o2 or o1==o3 or o2==o3:
        print("egyenlő szárú")
    else:
        print("csak szerkezthető")
else:
    print("Nem szerkezthető")