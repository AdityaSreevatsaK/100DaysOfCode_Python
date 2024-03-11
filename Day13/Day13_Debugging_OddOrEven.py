print("Day 13 - 100 Days of Code.")
print("Welcome to the Even or Odd Checker.")

number = int(input("Enter the number: ")) or 0

if number % 2 == 0:
    print(f"{number} is an even number.")
else:
    print(f"{number} is an odd number.")
