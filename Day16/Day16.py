import warnings

from Day15.coffee_machine_art import coffee_machine_logo
from coffee_maker import CoffeeMaker
from menu import Menu
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

with warnings.catch_warnings():
    warnings.simplefilter('ignore', SyntaxWarning)
    warnings.warn('bad', SyntaxWarning)
is_on = True
print("Day 16 - 100 Days of Code.")
print("Welcome to Coffee Machine.")
print(coffee_machine_logo)

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)

        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
