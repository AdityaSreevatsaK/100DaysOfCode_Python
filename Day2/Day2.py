print("Day 2 - 100 Days of Code.")
print("Welcome to Tip Calculator.")
billAmount = float(input("What is the total bill amount in Rupees?\n"))
zero = 0
tipPercentage = zero
tipGiven = input("Would you like to leave a tip (y/n)?\n")
if tipGiven.lower()[zero] == "y":
    tipPercentage = float(input("Enter the tip percentage. (Negative values will be considered 0): "))
    if tipPercentage < zero:
        tipPercentage = zero
numberOfMembers = int(input("How many people should the bill be split between?\n"))
amountPerMember = (billAmount + (billAmount * tipPercentage / 100)) / numberOfMembers
print("Each person should pay Rs. ", round(amountPerMember, 2))
