# szam=list(input())
# szam2=(int(szam[2])*100)+(int(szam[1])*10)+(int(szam[0]))
# print(szam2)

szam=int(input())
szam1=round((szam-szam%100)/100)
szam2=(szam%100)-(szam%10)
szam3=(szam%10)*100
eredmeny=szam3+szam2+szam1
print(eredmeny)

