x=int(input())
y=int(input())

if x>0 and y>0:
    print("I.síknegyed")
elif x<0 and y>0:
    print("II.síknegyed")
elif x<0 and y<0:
    print("III.síknegyed")
elif x>0 and y<0:
    print("IV.síknegyed")
elif x==0 and y!=0:
    print("y tengely")
elif y==0 and x!=0:
    print("x tengely")
else:
    print("Origó")
