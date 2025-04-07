from tkinter import *

print("Day 27 - 100 Days of Code.")
print("Welcome to Usage of Tkinter.")

window = Tk()
window.minsize(width=500, height=500)
my_label = Label(text="I am a new label", font=("Palatino Linotype", 15, 'italic'))
my_label.pack(side="top")


def when_button_clicked():
    my_label["text"] = "The button was clicked!"


button = Button(text="Click Me!", command=when_button_clicked)
button.pack(side="top")

window.mainloop()
