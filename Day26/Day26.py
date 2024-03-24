import pandas as pd

print("Day 26 - 100 Days of Code.")
print("Welcome to NATO Alphabet.")

nato_alphabet_data = pd.read_csv("nato_phonetic_alphabet.csv")
alphabet_calls = {row.iloc[0]: row.iloc[1] for index, row in nato_alphabet_data.iterrows()}
user_input = input("Enter your name:\n").upper()
name_nato_calls = []
for character in list(user_input):
    if character not in alphabet_calls.keys():
        continue
    name_nato_calls.append(alphabet_calls[character])
print("Your name in NATO Alphabet is as follows:")
for element in name_nato_calls:
    print(f"{element[0]} : {element}")
