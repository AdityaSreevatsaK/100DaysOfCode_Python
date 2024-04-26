import sys
from tkinter import *
from tkinter import messagebox

from QuizBrain import QuizBrain

THEME_COLOR = "#5356FF"
ZERO = 0
TWENTY = 20


class UserInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz_brain = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler App!")
        self.window.config(width=340, height=340, pady=TWENTY, padx=TWENTY, bg=THEME_COLOR)

        self.canvas = Canvas()
        self.canvas.config(width=300, height=250, bg="white")
        self.canvas.grid(row=1, column=ZERO, columnspan=2, pady=50)

        # Setting the width property makes the text go on to separate lines when length is greater than specified value.
        # Setting the fill property changes the colour of the text.
        self.question = self.canvas.create_text(150, 125, text="Question", fill="#0E46A3",
                                                font=("Palatino Linotype", 15, "italic"), width=280)

        self.score = Label(text="Score: 0", font=("Palatino Linotype", 15, "bold"), highlightthickness=ZERO,
                           bg=THEME_COLOR, fg="White")
        self.score.grid(row=ZERO, column=1)
        self.update_next_question()

        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=ZERO, pady=TWENTY, padx=TWENTY,
                                  command=self.is_false)
        self.true_button.grid(row=2, column=1)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=ZERO, pady=TWENTY, padx=TWENTY,
                                   command=self.is_true)
        self.false_button.grid(row=2, column=ZERO)

        self.window.mainloop()

    def update_next_question(self):
        """
            Method to update the next question onto the screen.
        """
        question_text = self.quiz_brain.next_question()
        if question_text is None:
            messagebox.showinfo(title="Completed quiz!", message=f"Your final score is {self.quiz_brain.score}/10!")
            self.window.after(1000, sys.exit(0))
        self.canvas.config(bg="white")
        self.canvas.itemconfig(self.question, text=question_text)

    def is_true(self):
        """
            Method to call the quiz brain class's method check answer when true button is selected.
        """
        if self.quiz_brain.check_answer("True"):
            self.change_canvas_colour("#C5FF95")
        else:
            self.change_canvas_colour("#F2613F")
        self.window.after(1000, self.update_next_question)

    def is_false(self):
        """
            Method to call the quiz brain class's method check answer when true button is selected.
        """
        if self.quiz_brain.check_answer("False"):
            self.change_canvas_colour("#C5FF95")
        else:
            self.change_canvas_colour("#F2613F")
        self.window.after(1000, self.update_next_question)

    def update_score(self):
        """
            Method to update the score onto the screen.
        """
        self.score["text"] = f"Score: {self.quiz_brain.score}"

    def change_canvas_colour(self, background_colour):
        """
            Method to change the canvas background colour based on the corresponding hex.
        """
        self.canvas.config(bg=background_colour)
        self.update_score()
