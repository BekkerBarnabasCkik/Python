szam=int(input())
szam1=szam//100
szam2=(szam-szam1*100)//10*10
szam3=(szam-(szam//100)*100)-((szam-szam//100*100)//10*10)
print(f"{szam3*100+szam2+szam1}")