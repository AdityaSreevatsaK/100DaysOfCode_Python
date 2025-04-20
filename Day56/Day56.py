from flask import Flask, render_template

print("Day 56 - 100 Days of Code.")
print("Welcome to Name Card.")

app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template('index.html')


if __name__ == "__main__":
    app.run()  # add argument debug=True when you want to see the change upon saving.
