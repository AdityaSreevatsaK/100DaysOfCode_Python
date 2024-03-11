print("Day 13 - 100 Days of Code.")
print("Welcome to the Leap Year Checker.")

zero = 0
hundred = 100
year = int(input("Enter the year to be checked: ")) or hundred

if (year % 400 == zero) and (year % hundred == zero):
    print(f"{year} is a leap year.")
elif (year % 4 == zero) and (year % hundred != zero):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
