import math

x1,y1,x2,y2 = [float(x) for x in input("Enter x1, y1, x2, y2 : ").split()]

length = abs((x1-x2)**2 + (y1-y2)**2)

print(math.sqrt(length),length)