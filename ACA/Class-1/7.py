curent_year = 2019
year = int(input("Enter year : "))
age = curent_year - year

if age < 0 or age > 120:
    print("Incorrect Year")
else:
    print(age)