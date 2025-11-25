#Be:
# 11:25
# 45
#Ki: 12 10
# ido=list(input())
# dogaido=int(input())

# tizesek=int(ido[3])
# egyesek=int(ido[4])

# oratizesek=int(ido[0])
# oraegyesek=int(ido[1])

# ora=oratizesek*10+oraegyesek

# perc=tizesek*10+egyesek

# if dogaido+perc>=60:    
#     perc2=(dogaido+perc)-(((perc+dogaido)//60)*60)
#     ora=ora+((dogaido+perc)//60)
# else:
#     perc2=dogaido+perc

# if perc2<10:
#     nulla=0
# else:
#     nulla=""
    
# print(f"{ora}:{nulla}{perc2}")

ido=list(input())
dogaido=int(input())

tizesek=int(ido[3])
egyesek=int(ido[4])

oratizesek=int(ido[0])
oraegyesek=int(ido[1])

ora=oratizesek*10+oraegyesek

perc=tizesek*10+egyesek

perc2=perc+dogaido-(((perc+dogaido)//60)*60)
ora=ora+((perc+dogaido)//60)

print(f"{ora}:{perc2:02}")



