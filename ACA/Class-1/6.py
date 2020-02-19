a,b = [int(x) for x in input("Enter a, b : ").split()]

# if a > b:
#     print(a,">",b)
# elif a < b:
#     print(a,"<",b)
# else:
#     print(a,"=",b)

print(a,">" if a>b else "<" if a<b else "=",b)