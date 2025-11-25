import math
a1=float(input())
a2=float(input())
a3=float(input())

h=3/(1/a1+1/a2+1/a3)
g=math.pow(a1*a2*a3,1/3)
a=(a1+a2+a3)/3
n=math.sqrt((a1*a1+a2*a2+a3*a3)/3)

print(round(h, 2))
print(round(g, 2))
print(round(a, 2))
print(round(n, 2))