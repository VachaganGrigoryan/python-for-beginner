a,b,c = [int(x) for x in input("Enter a, b, c : ").split()]

if a>b:
    if a>c:
        if b>c:
            a,c = c,a
        else:
            a,b,c = b,c,a
    else:
        a,b = b,a
elif b>c:
    if a>c:
        a,b,c = c,a,b
    else:
        b,c = c,b

print(a,' ',b,' ',c)