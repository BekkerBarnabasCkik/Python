#Be: float szám 156.456 2
#Ki: 156.45

import math
szam=float(input())
tizedes=int(input())
print(math.floor(szam*10**tizedes)/10**tizedes)
#156.456*10=1564.56

# a^-n == (1/a)^n