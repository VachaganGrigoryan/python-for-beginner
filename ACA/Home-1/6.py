px1,py1,px2,py2 = [int(i) for i in input("Enter px1, py1, px2, py2 [1:8] : ").split()]

dx = abs(px1-px2)
dy = abs(py1-py2)

if dx == 1 and dy == 2 or dx == 2 and dy == 1:
    print('Possible')
else:
    print('Impossible')