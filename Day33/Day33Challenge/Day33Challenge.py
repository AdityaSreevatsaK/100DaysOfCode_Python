from tkinter import *

import requests

kanye_quote = ""


def get_quote():
    global kanye_quote
    kanye_quote_response = requests.get(url="https://api.kanye.rest/")
    kanye_quote_response.raise_for_status()
    kanye_quote_response = kanye_quote_response.json()
    kanye_quote = kanye_quote_response["quote"]
    canvas.itemconfig(quote_text, text=kanye_quote)


print("Day 33 - 100 Days of Code.")
print("Welcome to Kanye Quotes!.")

window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text=kanye_quote, width=250, font=("Courier", 20, "bold"), fill="black")
get_quote()
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)

window.mainloop()
