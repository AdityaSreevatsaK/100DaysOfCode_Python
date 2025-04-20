import random

from flask import Flask

numbers_gif = "https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif"
correct_guess_gif = "https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif"
too_low_gif = "https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif"
too_high_gif = "https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif"

print("Day 55 - 100 Days of Code.")
print("Welcome to Higher Lower Game.")

app = Flask(__name__)

random_number = random.choice(range(0, 10))


@app.route('/')
def home_screen():
    return ('<h1 align="center">Hey there! Guess a number between 0 and 9 (both inclusive).<br/>'
            f'<img src="{numbers_gif}" alt="Numbers GIF." />')


@app.route('/<int:guess>')
def check_whether_correct_guess(guess):
    if guess == random_number:
        return ("<h1 align='center' style='color: green'>You found me!</h1><br/>"
                f"<div style='text-align: center;'>"
                f"<img align='center' src='{correct_guess_gif}' alt='Correct answer!' /></div>")
    elif guess < random_number:
        return ("<h1 align='center' style='color: blue'>Too low, try again.</h1><br/>"
                f"<div style='text-align: center;'>"
                f"<img align='center' src='{too_low_gif}' alt='Too low, try again.' /></div>")
    else:
        return ("<h1 align='center' style='color: red'>Too high, try again.</h1><br/>"
                f"<div style='text-align: center;'><img src='{too_high_gif}' alt='Too high, try again.' /></div>")


if __name__ == '__main__':
    app.run()  # add argument debug=True when you want to see the change as and when changed and saved.
