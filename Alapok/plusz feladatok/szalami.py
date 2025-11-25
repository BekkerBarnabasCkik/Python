#Be: 125468 dkg 
#Ki: ? t ? q (mázsa) ? kg ? dkg

szam1=int(input())
t=szam1//100000
maradek=szam1%100000
q=maradek//10000
maradek=maradek%10000
kg=maradek//100
maradek=maradek%100
dkg=maradek
print(f"{t} t {q} q {kg} kg {dkg} dkg")