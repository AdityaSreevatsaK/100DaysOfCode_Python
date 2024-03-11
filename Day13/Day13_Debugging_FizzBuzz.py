print("Day 13 - 100 Days of Code.")
print("Welcome to the FizzBuzz Program.")

zero = 0
three = 3
five = 5

for number in range(1, 101):
    if number % three == zero and number % five == zero:
        print("FizzBuzz")
    elif number % three == zero:
        print("Fizz")
    elif number % five == zero:
        print("Buzz")
    else:
        print(number)
