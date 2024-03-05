print("Day 2 - 100 Days of Code.")
print("Welcome to Tip Calculator.")
billAmount = float(input("What is the total bill amount in Rupees?\n"))
tipPercentage = 0
tipGiven = input("Would you like to leave a tip (y/n)?\n")
if tipGiven.lower()[0] == "y":
    tipPercentage = float(input("Enter the tip percentage. (Negative values will be considered 0): "))
    if tipPercentage < 0:
        tipPercentage = 0
numberOfMembers = int(input("How many people should the bill be split between?\n"))
amountPerMember = (billAmount + (billAmount * tipPercentage / 100)) / numberOfMembers
print("Each person should pay Rs. ", round(amountPerMember, 2))
