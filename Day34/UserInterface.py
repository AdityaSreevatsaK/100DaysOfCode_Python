from tkinter import *

THEME_COLOR = "#375362"


class UserInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler App!")
        self.window.config(width=340, height=340, pady=20, padx=20, bg=THEME_COLOR)

        self.canvas = Canvas()
        self.canvas.config(width=300, height=250, bg="white")
        self.canvas.grid(row=1, column=0, columnspan=2)

        self.question = self.canvas.create_text(150, 125, text="Question Text",
                                                font=("Palatino Linotype", 15, "italic"))

        self.score = Label(text="Score: 0", font=("Palatino Linotype", 15, "italic"), highlightthickness=0, pady=20,
                           padx=20, bg=THEME_COLOR, fg="White")
        self.score.grid(row=0, column=1)

        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, pady=30, padx=30)
        self.true_button.grid(row=2, column=1)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, pady=30, padx=30)
        self.false_button.grid(row=2, column=0)

        self.window.mainloop()
