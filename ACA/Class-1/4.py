n, an, m, am, k = [int(x) for x in input("Enter value n, an, m, am and k : ").split()]

# an = a1 + (n-1)d
# am = a1 + (m-1)d
# a1 = an - (n-1)d
# a1 =  am - (m-1)d
# an - (n-1)d = am - (m-1)d
# an - am = (n-1)d - (m-1)d
# an - am = ((n-1) - (m-1))d

d = (an-am)/((n-1) - (m-1))
a1 = an - (n-1)*d
ak = a1 + (k-1)*d

print(ak)