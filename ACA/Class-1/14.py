a1,b1,a2,b2 = [float(x) for x in input("Enter a1, b1, a2, b2 : ").split()]

if a1<a2 and a2<b1 or a2<a1 and a1<b2:
    print(abs(a1-a2),"One")
elif a2<b1 and b1<b2 or b1<a2 and a2<a1 :
    print(abs(a2-b1),"Two")
elif b1<b2 and b2<a1 or b2<b1 and b1<a2:
    print(abs(b1-b2),"Three")
elif a1<b2 and b2<b1 or b2<a1 and a1<a2:
    print(abs(a1-b2),"Four")
else:
    print(0,"Six")
