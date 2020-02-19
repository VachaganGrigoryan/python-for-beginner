import math
a,b,c = [float(x) for x in input("Enter a, b, c value: ").split()]

if a != 0:
    # if a is nonzero, the equation is quadratic
    print("Quadratic equation")
    D = b*b - 4*a*c;
    print("Discriminant: ",D)
    if D>0:
        x1 = (-b - math.sqrt(D))/(2*a)
        x2 = (-b + math.sqrt(D))/(2*a)
        print("Two solutions: ",x1," ",x2)
    elif D == 0.0 or D == -0.0:
        x = -b/(2*a)
        print("One solution: ",x)
    else:
        print("No solutions")
else:
    print("Non-quadratic equation")
    if b != 0:
        print("One solution: ",-c/b)
    elif c == 0:
        print("Infinite solutions")
    else:
        print("No solutions")