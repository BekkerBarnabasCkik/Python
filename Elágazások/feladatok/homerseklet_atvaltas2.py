# import math
# mertek=str(input())
# szam1=float(input())
# kiMertek=str(input())

# if mertek=="f":
#     c=(((szam1-32)*5)/9)
# elif mertek=="c":
#     f=((szam1*9)/5)+32

# if mertek=="f" and kiMertek=="c":
#     print(print(math.floor(c*100)/100))
# elif mertek=="f" and kiMertek=="k":
#     print(c+273.15)
# elif mertek=="c" and kiMertek=="f":
#     print((c*9)/5+32)
# elif mertek=="c" and kiMertek=="k":
#     print(c+273,15)
# elif mertek=="k" and kiMertek=="c":
#     print=()

import math
m=str(input())
fok=int(input())
m2=str(input())

c=0
if m=="f":
    c=(fok-32)*5/9
elif m=="k":
    fok-273.15
else:
    c=fok

if m2=="f":
    print(math.floor((c*9/5+32)*100)/100)
elif m2=="k":
    print(c+273.15)
else:  
    print(c)