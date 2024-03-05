import random

print("Day 5 - 100 Days of Code.")
print("Welcome to the Password Generator.")
number_of_letters = int(input("How many letters would you like in your password?\n"))
number_of_symbols = int(input("How many symbols would you like in your password?\n"))
number_of_numbers = int(input("How many numbers would you like in your password?\n"))

passwordList = []

for iterator in range(number_of_letters):
    random_character = random.randint(65, 122)
    if random_character in range(91, 97):
        random_character += random.randint(10, 30)
    passwordList.append(chr(random_character))

for iterator in range(number_of_symbols):
    passwordList.append(chr(random.randint(33, 48)))

for iterator in range(number_of_numbers):
    passwordList.append(chr(random.randint(0, 9)))

random.shuffle(passwordList)
password = ""
for element in passwordList:
    password += element

print("Your new password is", password)
