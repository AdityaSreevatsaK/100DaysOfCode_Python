from tkinter import *

print("Day 29 - 100 Days of Code.")
print("Welcome to Password Manager.")

ZERO = 0
ONE = 1
TWO = 2
BACKGROUND_COLOUR = "#FFF6E9"
font_tuple = ("Palatino Linotype", 10, "bold")


def save_data_after_validation():
    """
        Method to perform validations on the fields and save the same into the file.
    """
    print("Okay")
    print("website_entry", str(website_entry), type(str(website_entry)))
    print("email_username_entry", str(email_username_entry))
    print("password_entry", str(password_entry))


window = Tk()
window.config(padx=100, pady=100, bg=BACKGROUND_COLOUR)
window.title("Password Manager")

canvas = Canvas(width=200, height=200, bg=BACKGROUND_COLOUR, highlightthickness=ZERO)
password_manager_logo = PhotoImage(file="PasswordManagerLogo.png")
canvas.create_image(100, 100, image=password_manager_logo)
canvas.grid(column=ONE, row=ZERO)

website_field_name = Label(text="Website:", font=font_tuple, bg=BACKGROUND_COLOUR, highlightthickness=ZERO)
website_field_name.grid(column=ZERO, row=ONE)

website_entry = Entry(width=52)
website_entry.focus()  # When the program starts, the cursor directly starts off in that entry box.
website_entry.grid(column=ONE, row=ONE, columnspan=TWO)

email_username_field_name = Label(text="Email ID/ Username:", font=font_tuple,
                                  bg=BACKGROUND_COLOUR, highlightthickness=ZERO)
email_username_field_name.grid(column=ZERO, row=TWO)

email_username_entry = Entry(width=52)
email_username_entry.insert(0, "ASK@email.com")
email_username_entry.grid(column=ONE, row=TWO, columnspan=TWO)

password_field_name = Label(text="Password:", font=font_tuple, bg=BACKGROUND_COLOUR, highlightthickness=ZERO)
password_field_name.grid(column=ZERO, row=3)

password_entry = Entry(width=32)
password_entry.grid(column=ONE, row=3)

generate_password_button = Button(text="Generate Password.")
generate_password_button.grid(column=TWO, row=3)

add_button = Button(text="Add.", width=45, command=save_data_after_validation)
add_button.grid(column=ONE, row=4, columnspan=TWO)

window.mainloop()
