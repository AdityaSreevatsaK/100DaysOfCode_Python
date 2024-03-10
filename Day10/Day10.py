import warnings

from calculator_art import calculator_logo

with warnings.catch_warnings():
    warnings.simplefilter('ignore', SyntaxWarning)
    warnings.warn('bad', SyntaxWarning)
print("Day 10 - 100 Days of Code.")
print("Welcome to the Calculator App.")
print(calculator_logo)

number_one = float(input("Enter the first number:\n"))
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
operation = int(input("Enter the operation to be performed - 1,2,3 or 4:\n"))
number_two = float(input("Enter the second number:\n"))

if operation == 1:
    print(f"The sum of {number_one} and {number_two} is {number_one + number_two}")
elif operation == 2:
    print(f"The difference between {number_one} and {number_two} is {number_one - number_two}")
elif operation == 3:
    print(f"The product of {number_one} and {number_two} is {number_one * number_two}")
elif operation == 4:
    try:
        print(f"The quotient of {number_one} by {number_two} is {number_one / number_two}")
    except ZeroDivisionError:
        print("♾️. Anything divided by zero is Infinity.")
else:
    print("Invalid operation entered.")
