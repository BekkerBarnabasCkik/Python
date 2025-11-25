import math
szam1=float(input())
szam2=float(input())
szam3=float(input())
H=3/(1/szam1+1/szam2+1/szam3)
G=math.pow(szam1*szam2*szam3,1/3)
A=(szam1+szam2+szam3)/3
N=math.sqrt((szam1*szam1+szam2*szam2+szam3*szam3)/3)
print(f"H: {round(H, 2)}")
print(f"G: {round(G, 2)}")
print(f"A: {round(A, 2)}")
print(f"N: {round(N, 2)}")