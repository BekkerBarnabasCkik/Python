szam=int(input("Írj be egy számot: "))
ezresek=szam//1000
szazasok=(szam%1000)//100
tizesek=(szam%100)//10
egyesek=szam%10
print(f"{ezresek+szazasok+tizesek+egyesek}")