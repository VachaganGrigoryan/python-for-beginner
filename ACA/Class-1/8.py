a,b,c = [int(x) for x in input("Enter a, b, c : ").split()]

if((a >= b and b >= c) or (a <= b and b <= c) ):
    print("Sorted")
else:
    print("Unsorted")