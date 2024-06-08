import turtle
from turtle import Screen

print("Day 25 - 100 Days of Code.")
print("Welcome to India States Game.")
counter = 0
comma = ","
screen = Screen()
screen.setup(width=700, height=700)
screen.title("India States Game!")
screen.bgpic(picname="India Map.gif")
state_list = ["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", "Haryana",
              "Himachal Pradesh", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur",
              "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana",
              "Tripura", "Uttarakhand", "Uttar Pradesh", "West Bengal", "Andaman and Nicobar Islands", "Chandigarh",
              "Dadra and Nagar Haveli", "Daman and Diu", "Delhi", "Jammu and Kashmir", "Ladakh", "Lakshadweep"]


def get_mouse_click_coordinates(x, y):
    """
    Description:
        Method to get the c and y coordinates of the states.
        The x and y values are printed each time the mouse is clicked.
    """
    global counter
    string_value = state_list[counter] + comma + str(x) + comma + str(y) + "\n"
    print(string_value, end="")
    counter += 1


screen.onscreenclick(get_mouse_click_coordinates)
turtle.mainloop()
