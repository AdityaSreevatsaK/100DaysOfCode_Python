print("Day 26 - 100 Days of Code.")
print("Welcome to Day 26 - Challenges.")

print("Challenge 1 - List Comprehension - Squaring Numbers using list comprehension.")
squared_list = [number ** 2 for number in range(0, 16)]
print("Squared List:", squared_list)

print("Challenge 2 - List Comprehension - Filtering even numbers.")
even_list = [number for number in range(0, 16) if number % 2 == 0]
print("List with even numbers:", even_list)

print("Challenge 3 - List Comprehension - Data Overlap.")
with open("file1.txt", mode="r") as file1:
    file1_content = file1.readlines()
with open("file2.txt", mode="r") as file2:
    file2_content = file2.readlines()
data_overlap = [int(number) for number in file1_content if number in file2_content]
print("Numbers present on both files:", data_overlap)

print("Challenge 1 - Dictionary Comprehension - Length of words in a sentence.")
user_input = input("Enter a sentence:\n")
user_input_list = user_input.split(" ")
number_of_occurrences = {word: len(word) for word in user_input_list}
for key, value in number_of_occurrences.items():
    print(f"{key} : {value}")

print("Challenge 2 - Dictionary Comprehension - Convert list of week's temperature to Celsius.")
temperature_fahrenheit = {"Monday": 53.5, "Tuesday": 57.2, "Wednesday": 59, "Thursday": 57.2, "Friday": 69.8,
                          "Saturday": 71.6, "Sunday": 75.2}
temperature_celsius = {day: (temperature - 32) / 1.8 for day, temperature in temperature_fahrenheit.items()}
print("Temperature for the week in Celsius.")
for day, temperature in temperature_celsius.items():
    print(f"{day}: {temperature}")
