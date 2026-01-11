# import random

# hossz=int(input())
# mettol=int(input())
# meddig=int(input())

# def kiiras(t):
#     for i in range(0, len(t), 1):
#         if i!=len(t)-1:
#             print(t[i], end=",")
#         else:
#             print(t[i])

# def tombfeltoltes(n, a, b):
#     t=[]
#     for i in range(n):
#         t.append(random.randint(a, b))
    
#     return t

# t=tombfeltoltes(hossz, mettol, meddig)
# kiiras(t)

#----------------------11.Feladat------------------------
import random

n=int(input())
t=[0]

def tombfeltoltes(n, t):
    for i in range(n-2):
        t.append(random.randint(1, 1000))
    t.append(0)

    return t

magassagok=tombfeltoltes(n, t)

def maximum(tömb):
    maxi=0
    for i in range(len(tömb)):
        if tömb[i]>tömb[maxi]:
            maxi=i
    
    return maxi

maxi=maximum(magassagok)

def kiiras(tömb):
    for i in range(len(tömb)):
        if i!=len(t)-1:
            print(t[i], end=",")
        else:
            print(t[i])

kiiras(magassagok)
print()
print(f"A legmagasabb pont a {maxi+1}. helyen volt")


