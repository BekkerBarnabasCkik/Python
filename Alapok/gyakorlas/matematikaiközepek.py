import math
szam1=float(input())
szam2=float(input())
szam3=float(input())
H=3/(1/szam1+1/szam2+1/szam3)
M=pow(szam1*szam2*szam3, 1/3)
A=(szam1+szam2+szam3)/3
N=math.sqrt((pow(szam1, 2)+pow(szam2, 2)+pow(szam3, 2))/3)
print(round(H, 2))
print(round(M, 2))
print(round(A, 2))
print(round(N, 2))