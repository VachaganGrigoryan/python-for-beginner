a, b, c = [int(x) for x in input("Enter a, b, c value: ").split()]

if(a>b and a>c):
    a,c = c,a
elif (b>c):
    b,c = c,b

if (a+b>c):
    if(a*a+b*b==c*c):
        print("Right Triangle")
    elif (a*a+b*b>c*c):
        print("Obtuse Triangle")
    else:
        print("Acute Triangle")
else:
    print("No Triangle")
