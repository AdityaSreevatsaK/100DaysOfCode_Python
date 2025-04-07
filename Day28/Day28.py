import math
from tkinter import *

FOREGROUND_COLOUR = "#40A2E3"
BACKGROUND_COLOUR = "#FFE4C9"
WHITE = "white"
PL_FONT = "Palatino Linotype"
BOLD = "bold"
ITALIC = "italic"
ZERO = 0
ONE = 1
TWO = 2
SIXTY = 60
SHORT_BREAK_TIME_MINUTES = 5
LONG_BREAK_TIME_MINUTES = 20
WORK_TIME_MINUTES = 25
HUNDRED = 100
count_timer = 5
WORK_ITERATIONS = ZERO
COUNTER = ZERO
TIMER = ''

print("Day 28 - 100 Days of Code.")
print("Welcome to Pomodoro App.")


def start_pomodoro_timer():
    """
        Method to start the pomodoro app.
    """
    global WORK_ITERATIONS
    WORK_ITERATIONS += ONE
    if WORK_ITERATIONS % 8 == ZERO:
        title_label.config(text="Break! :)", fg="#430A5D")
        add_new_checkmark()
        count_down(LONG_BREAK_TIME_MINUTES * SIXTY)
    elif WORK_ITERATIONS % TWO == ZERO:
        title_label.config(text="Break! :)", fg="#FE7A36")
        add_new_checkmark()
        count_down(SHORT_BREAK_TIME_MINUTES * SIXTY)
    else:
        title_label.config(text="Work.", fg="#D63484")
        count_down(WORK_TIME_MINUTES * SIXTY)
    title_label.grid(column=TWO, row=ZERO)


def reset_pomodoro_timer():
    """
        Method to reset the pomodoro app.
    """
    global TIMER
    try:
        window.after_cancel(TIMER)
    except ValueError:
        pass
    global WORK_ITERATIONS
    WORK_ITERATIONS = ZERO
    checkmark_label["text"] = ""
    checkmark_label.grid(column=TWO, row=TWO)
    canvas.itemconfig(timer_text, text="00:00")
    canvas.grid(column=TWO, row=ONE)
    title_label["text"] = "Timer"
    title_label.grid(column=TWO, row=ZERO)


def add_new_checkmark():
    """
        Method to add a new checkmark after one iteration.
    """
    checkmark_label["text"] = "✓" * math.floor(WORK_ITERATIONS / TWO)
    checkmark_label.grid(column=TWO, row=TWO)
    canvas.itemconfig(timer_text, text="00:00")
    canvas.grid(column=TWO, row=ONE)


def count_down(count_value):
    """
        Method that starts the countdown for one iteration.
    """
    global count_timer
    if count_value >= ZERO:
        count_value_minute = math.floor(count_value / 60)
        count_value_second = count_value % 60
        if count_value_second in range(ZERO, 10):
            count_value_second = str(ZERO) + str(count_value_second)
        count_timer -= ONE
        canvas.itemconfig(timer_text, text=f"{count_value_minute}:{count_value_second}")
        global TIMER
        TIMER = window.after(10, count_down, count_value - ONE)
    else:
        start_pomodoro_timer()


window = Tk()
window.title("Pomodoro App.")
window.config(padx=HUNDRED, pady=HUNDRED, bg=BACKGROUND_COLOUR)

canvas = Canvas(width=210, height=233, bg=BACKGROUND_COLOUR, highlightthickness=ZERO)
tomato_image = PhotoImage(file="Tomato.png")
canvas.create_image(HUNDRED, HUNDRED, image=tomato_image)
timer_text = canvas.create_text(HUNDRED, 120, text="00:00", font=(PL_FONT, 25, ITALIC), fill=WHITE)
canvas.grid(column=TWO, row=ONE)

title_label = Label(text="Timer", font=("Courier", 30, BOLD), bg=BACKGROUND_COLOUR, fg=FOREGROUND_COLOUR)
title_label.grid(column=TWO, row=ZERO)

start_button = Button(text="Start", font=(PL_FONT, 10, ITALIC), bg=WHITE, command=start_pomodoro_timer)
start_button.grid(column=ONE, row=TWO)

reset_button = Button(text="Reset", font=(PL_FONT, 10, ITALIC), bg=WHITE, command=reset_pomodoro_timer)
reset_button.grid(column=3, row=TWO)

checkmark_label = Label(text="✓", font=(PL_FONT, 20, "normal"), bg=BACKGROUND_COLOUR, fg=FOREGROUND_COLOUR)

window.mainloop()
