betu=input().lower()
tolas=int(input())
print(chr((ord(betu)-ord("a") + tolas) % 26 + ord("a")))
 