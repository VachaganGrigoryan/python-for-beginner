a,b,c = [int(x) for x in input("Enter a, b, c : ").split()]

# print(max(a,b,c)-min(a,b,c))

if a>b:
    if a>c:
        if b>c:
            print(a-c)
        else:
            print(a-b)
    else:
        print(c-b)
elif b>c:
    if a>c:
        print(b-c)
    else:
        print(b-a)
else:
    print(c-a)