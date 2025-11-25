szam=input()
adatok=szam.split()
fej1=int(adatok[0])
fej2=int(adatok[1])
osszfej=int(adatok[2])
i=1
while (osszfej-i*fej1)%fej2!=0:
    i+=1
print(i, round((osszfej-i*fej1)/fej2))