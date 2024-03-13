import warnings

import coffee_machine_data
from coffee_machine_art import coffee_machine_logo

with warnings.catch_warnings():
    warnings.simplefilter('ignore', SyntaxWarning)
    warnings.warn('bad', SyntaxWarning)

print("Day 15 - 100 Days of Code.")
print("Welcome to Coffee Machine.")
print(coffee_machine_logo)

zero = 0
does_user_wish_to_continue = True
cost = "cost"
ingredients = "ingredients"
drink_choices = ["espresso", "latte", "cappuccino"]
quarters = zero
dimes = zero
nickels = zero
pennies = zero


def get_coffee_maker_report():
    """
    Description:
        Method to get the report for the coffee maker. The profits and resources available.
    """
    print(f"Profits: ${coffee_machine_data.profit}")
    print("Resources:")
    for ingredient, volume in coffee_machine_data.resources.items():
        print(f"{ingredient} : {volume}ml")


def calculate_profits(drink_choice):
    """
    Description:
        Method to calculate the profits after current order.
    """
    print("coffee_machine_data.MENU[drink_choice][cost]", coffee_machine_data.MENU[drink_choice][cost])
    coffee_machine_data.profit += coffee_machine_data.MENU[drink_choice][cost]


def calculate_remaining_resources(drink_choice):
    """
    Description:
        Method to calculate the remaining resources after current order.
    """
    ingredients_volume = coffee_machine_data.MENU[drink_choice][ingredients]
    print(ingredients_volume)
    water = "water"
    milk = "milk"
    coffee = "coffee"
    water_volume = ingredients_volume[water]
    milk_volume = ingredients_volume[milk]
    coffee_volume = ingredients_volume[coffee]

    coffee_machine_data.resources[water] -= water_volume
    coffee_machine_data.resources[milk] -= milk_volume
    coffee_machine_data.resources[coffee] -= coffee_volume


def change_calculation(cost_of_drink, amount_deposited, drink_choice):
    """
    Description:
        Method to calculate and output the difference between amount deposited and the cost of the beverage.
    """
    change = round(amount_deposited - cost_of_drink, 2)
    if change == zero:
        print(f"Enjoy your {drink_choice}. 🍵")
    else:
        print(f"Enjoy your {drink_choice} 🍵. Change of ${change} returned.")


def get_drink_details(drink_name):
    """
    Description:
        Method to fetch the details of a particular drink.
    Return:
        float:  Cost of drink.
        dict:   A dictionary containing ingredients for said drink.
    """
    drink_details = coffee_machine_data.MENU[drink_name]
    return drink_details[cost], drink_details[ingredients]


def display_cost_of_drinks():
    """
    Description:
        Method to print the drink type and associated cost.
    """
    for drink_name, drink_details in coffee_machine_data.MENU.items():
        print(f"{drink_name.title()} costs ${drink_details[cost]}.")
    return None


def is_resources_enough_for_current_order(current_order):
    """
    Description:
        Method to check if the resources available are enough to complete the current order.

    Return:
        bool:   If resources will suffice, True.
        str:    If resources will not suffice, the name of the resource which is in deficit.
    """
    drink_details = coffee_machine_data.MENU[current_order]
    for component, component_volume in drink_details[ingredients].items():
        if coffee_machine_data.resources[component] < component_volume:
            return component
    return True


while does_user_wish_to_continue:
    display_cost_of_drinks()
    user_choice = None
    while True:
        print("Please enter 'report' to view coffee maker report.")
        user_choice = input(
            "Please enter which drink you would like. Options are:\n1. Espresso\n2. Latte\n3. Cappuccino\n").lower()
        if user_choice == 'report':
            get_coffee_maker_report()
        if user_choice in drink_choices:
            break

    is_resource_deficit = is_resources_enough_for_current_order(user_choice)
    if is_resource_deficit in drink_choices:
        print("Sorry. There is not enough", is_resource_deficit)
        continue
    try:
        quarters = int(input("Please enter the number of quarters: "))
        dimes = int(input("Please enter the number of dimes: "))
        nickels = int(input("Please enter the number of nickels: "))
        pennies = int(input("Please enter the number of pennies: "))
    except ValueError as e:
        print("Invalid value entered.")
    total_amount_deposited = quarters * 0.25 + dimes * 0.1 + nickels * 0.05 + pennies * 0.01
    drink_cost, drink_ingredients = get_drink_details(user_choice)
    if total_amount_deposited < drink_cost:
        print(f"Sorry. Money is not enough. A total of ${total_amount_deposited} refunded.")
        continue
    change_calculation(drink_cost, total_amount_deposited, user_choice)
    calculate_remaining_resources(user_choice)
    calculate_profits(user_choice)
