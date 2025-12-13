t=[1,2,23,456]
osszes=0
def proba(t, osszes):
    for i in range(len(t)):
        if t[i]>10:
            osszes+=1
    return(osszes)
print(proba(t,0))
