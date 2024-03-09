import random

print("Day 4 - 100 Days of Code.")
print("Welcome to Rock, Paper and Scissors.")

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

zero = 0
two = 2
userChoice = int(input("What do you choose? Type 0 : Rock, 1 : Paper, 2 : Scissors.\n"))
yourChoiceString = "Your choice:\n"
computersChoiceString = "Computer choice:\n"
youLoseString = "You lose. 😭"
youWinString = "You win! 😉"

computerChoice = random.randint(zero, two)
rockPaperScissor = [rock, paper, scissors]

if userChoice > two or userChoice < zero:
    print("You typed an invalid number." + youLoseString)
else:
    print(yourChoiceString, rockPaperScissor[userChoice])
    print(computersChoiceString, rockPaperScissor[computerChoice])
    if userChoice == zero and computerChoice == two:
        print(youWinString)
    elif computerChoice == zero and userChoice == two:
        print(youLoseString)
    elif computerChoice > userChoice:
        print(youLoseString)
    elif userChoice > computerChoice:
        print(youWinString)
    elif computerChoice == userChoice:
        print("It's a draw. 🫤")
