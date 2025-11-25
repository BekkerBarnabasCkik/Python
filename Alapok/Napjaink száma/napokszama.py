mostev=int(input())
mosthonap=int(input())
mostnap=int(input())

szulev=int(input())
szulhonap=int(input())
szulnap=int(input())

mostcsaknap=mostev*365+mosthonap*30+mostnap
szuletescsaknap=szulev*365+szulhonap*30+szulnap
print(f"Születésünk óta eltelt napok száma: {mostcsaknap-szuletescsaknap}")