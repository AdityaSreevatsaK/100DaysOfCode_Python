import sys
from random import choice
from tkinter import *
from tkinter import messagebox

import pandas as pd

print("Day 31 - 100 Days of Code.")
print("Welcome to Flash Card App - Capstone Project.")

ZERO = 0
ONE = 1
TWO = 2
BACKGROUND_COLOUR = "#B1DDC6"
PALATINO_LINOTYPE = "Palatino Linotype"
ENGLISH = "English"
FRENCH = "French"
DISPLAYED_WORDS_FILE = "data/DisplayedWords.txt"
SCORE = ZERO
TOTAL = ZERO
EMPTY_STRING = ""
NEW_LINE = "\n"
CURRENT_FRENCH_WORD = EMPTY_STRING
CURRENT_ENGLISH_WORD = EMPTY_STRING
CURRENT_SCREEN = EMPTY_STRING

fr_eng = pd.read_csv("data/FrenchToEnglish.csv")
FR_ENG_DATA = fr_eng.to_dict(orient="tight")["data"]


def change_image():
    """
        Method to change the image.
    """
    global CURRENT_SCREEN
    canvas.itemconfig(card_image, image=back_image)
    canvas.itemconfig(language_word, text=ENGLISH, fill="white")
    canvas.itemconfig(french_english_word, text=CURRENT_ENGLISH_WORD, fill="white")
    CURRENT_SCREEN = ENGLISH


def change_word_on_screen():
    """
        Method to change the word on the screen to French.
    """
    global CURRENT_FRENCH_WORD, CURRENT_ENGLISH_WORD, CURRENT_SCREEN
    try:
        CURRENT_FRENCH_WORD, CURRENT_ENGLISH_WORD = choice(FR_ENG_DATA)
        with open(DISPLAYED_WORDS_FILE, mode="r") as displayed_words:
            while CURRENT_FRENCH_WORD in displayed_words and CURRENT_FRENCH_WORD != EMPTY_STRING:
                CURRENT_FRENCH_WORD, CURRENT_ENGLISH_WORD = choice(FR_ENG_DATA)
            else:
                with open(DISPLAYED_WORDS_FILE, mode="a") as shown_words:
                    shown_words.write(CURRENT_FRENCH_WORD + NEW_LINE)
    except FileNotFoundError:
        print("Encountered file not found exception.")
    except IndexError:
        exit_game()
    else:
        FR_ENG_DATA.remove([CURRENT_FRENCH_WORD, CURRENT_ENGLISH_WORD])
        canvas.itemconfig(card_image, image=front_image)
        canvas.itemconfig(language_word, text=FRENCH, fill="black")
        canvas.itemconfig(french_english_word, text=CURRENT_FRENCH_WORD, fill="black")
        CURRENT_SCREEN = FRENCH
        canvas.after(3000, change_image)


def correct_answer():
    """
        Method to increase the score and total value and call the screen change method.
    """
    if CURRENT_SCREEN == FRENCH:
        pass
    else:
        global SCORE, TOTAL
        SCORE += ONE
        TOTAL += ONE
        change_word_on_screen()


def incorrect_answer():
    """
        Method to increase the total value and call the screen change method.
    """
    if CURRENT_SCREEN == FRENCH:
        pass
    else:
        global TOTAL
        TOTAL += ONE
        change_word_on_screen()


def exit_game():
    """
        Method to display the score and exit the game.
    """
    messagebox.showinfo(title="Exiting game.", message=f"Score: {SCORE}/{TOTAL}")
    print(f"Score: {SCORE}/{TOTAL}")
    try:
        window.after(2000, window.destroy())
    except TclError:
        pass
    displayed_words_file = open(DISPLAYED_WORDS_FILE, mode="r+")
    displayed_words_file.seek(ZERO)
    displayed_words_file.truncate()
    sys.exit(ZERO)


window = Tk()
window.config(padx=200, pady=50, bg=BACKGROUND_COLOUR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOUR, highlightthickness=ZERO)
front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
card_image = canvas.create_image(400, 263, image=front_image)
canvas.grid(row=ZERO, column=ZERO, columnspan=TWO)
language_word = canvas.create_text(400, 150, text=FRENCH, font=(PALATINO_LINOTYPE, 40, "italic"))
french_english_word = canvas.create_text(400, 263, text="WORD", font=(PALATINO_LINOTYPE, 60, "bold"))

right_image = PhotoImage(file="images/right.png")
correct_button = Button(image=right_image, highlightthickness=ZERO, bg=BACKGROUND_COLOUR, command=correct_answer)
correct_button.grid(row=ONE, column=ONE)

left_image = PhotoImage(file="images/wrong.png")
incorrect_button = Button(image=left_image, highlightthickness=ZERO, bg=BACKGROUND_COLOUR, command=incorrect_answer)
incorrect_button.grid(row=ONE, column=ZERO)

exit_image = PhotoImage(file="images/exit.png")
exit_game_button = Button(image=exit_image, highlightthickness=ZERO, bg=BACKGROUND_COLOUR, command=exit_game)
exit_game_button.grid(row=TWO, column=ZERO, columnspan=TWO)

change_word_on_screen()
window.mainloop()
exit_game()
