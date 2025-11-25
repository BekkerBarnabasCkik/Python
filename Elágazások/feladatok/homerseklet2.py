import math
bem=str(input())
f=float(input())
kim=str(input())
c=0
if bem=="f":
    c=((f-32)*5)/9
elif bem=="k":
    c=f-273.15
else:
    c=f

if kim=="f":
    e=c*9/5+32
elif kim=="k":
    e=c+273.15
else:
    e=c
print(math.floor(e*100)/100)
