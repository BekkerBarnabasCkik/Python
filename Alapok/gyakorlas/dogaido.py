ora=int(input())
perc=int(input())
dogaido=int(input())
ora=ora+((perc+dogaido)//60)
perc=perc+dogaido-(perc+dogaido)//60*60
print(f"{ora}:{perc:02}")