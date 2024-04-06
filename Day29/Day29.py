from random import choice, randint, shuffle
from tkinter import *
from tkinter import messagebox

import pyperclip

print("Day 29 - 100 Days of Code.")
print("Welcome to Password Manager.")

ZERO = 0
ONE = 1
TWO = 2
THREE = 3
EMPTY_STRING = ""
BACKGROUND_COLOUR = "#B3C8CF"
font_tuple = ("Palatino Linotype", 10, "bold")


def save_data_after_validation():
    """
        Method to perform validations on the fields and save the same into the file.
    """
    website = website_entry.get().title()
    email = email_username_entry.get().lower()
    password = password_entry.get()
    pipe_symbol = " | "
    if website == EMPTY_STRING:
        messagebox.showerror(title="Blank field(s).", message="Website field is empty.")
        return
    elif password == EMPTY_STRING:
        messagebox.showerror(title="Blank field(s).", message="Password field is empty.")
        return
    elif email == EMPTY_STRING:
        messagebox.showerror(title="Blank field(s).", message="Email field is empty.")
        return
    elif " " in password:
        messagebox.showerror(title="Invalid entry.", message="Password field has a whitespace.")
        return
    else:
        pass

    confirm_addition = messagebox.askyesno(title="Are these values correct?", message=f"Website: {website}\n"
                                                                                      f"Email ID / Username: {email}\n"
                                                                                      f"Password: {password}")
    if confirm_addition:
        try:
            with open(file="Passwords.txt", mode="a") as passwords_file:
                passwords_file.write(website + pipe_symbol + email + pipe_symbol + password + pipe_symbol + "\n")
        except FileNotFoundError:
            print("Exception encountered.")
        else:
            messagebox.showinfo(title="Added.", message="Addition successful.")
    else:
        pass


def generate_randomised_password():
    """
        Method to generate a random 12 character password.
    """
    randomised_password = []
    password_length = 12
    special_characters = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "+", "-", "_"]
    for iterator in range(int(password_length / 4)):
        randomised_password.append(choice(special_characters))
        randomised_password.append(chr(randint(65, 90)))
        randomised_password.append(str(randint(ZERO, 9)))
        randomised_password.append(chr(randint(97, 122)))
    shuffle(randomised_password)
    password_entry.delete(ZERO, 13)
    password = EMPTY_STRING.join([character for character in randomised_password])
    pyperclip.copy(password)
    password_entry.insert(ZERO, password)


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
email_username_entry.insert(ZERO, "ASK@email.com")
email_username_entry.grid(column=ONE, row=TWO, columnspan=TWO)

password_field_name = Label(text="Password:", font=font_tuple, bg=BACKGROUND_COLOUR, highlightthickness=ZERO)
password_field_name.grid(column=ZERO, row=THREE)

password_entry = Entry(width=32)
password_entry.grid(column=ONE, row=THREE)

generate_password_button = Button(text="Generate Password.", command=generate_randomised_password)
generate_password_button.grid(column=TWO, row=THREE)

add_button = Button(text="Add.", width=45, command=save_data_after_validation)
add_button.grid(column=ONE, row=4, columnspan=TWO)

window.mainloop()
