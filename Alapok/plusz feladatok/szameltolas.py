betu=input().lower()
eltolas=int(input())
eredmeny=chr((ord(betu)-ord("a") + eltolas) % 26 + ord("a"))
print(eredmeny) 

# b-98
# 98+6=104-97=7 7%26=7+97=104

#a=97
#A=