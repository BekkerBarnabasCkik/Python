f=open("proba.txt")
t=f.read()
f.close()
hatarok=[]
ertekek=[]
valtas=False
for i in range(len(t)):
    if valtas==False:
        if t[i]=="\n" and t[i+1]=="\n":
            valtas=True
        else:
            hatarok.append(t[i])
    else:
        ertekek.append(t[i])
print(hatarok,ertekek)


for i in range(len(hatarok)):
    alsoertek=0
    felsoertek=0
    alsoszamjegyek=[]
    while i<len(hatarok) and hatarok[i]!="-" and hatarok[i]!="\n":
        alsoszamjegyek.append(hatarok[i])
        i+=1
    i+=len(alsoszamjegyek)-1
    print(alsoszamjegyek)
    


