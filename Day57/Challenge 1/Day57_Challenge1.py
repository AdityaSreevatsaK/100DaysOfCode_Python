from datetime import datetime

from flask import Flask, render_template

print("Day 57 Challenge - 100 Days of Code.")
print("Welcome to Dynamic values being passed from python to HTML.")

app = Flask(__name__)


@app.route('/')
def home():
    """
    Renders the home page with the current year dynamically passed to the HTML template.

    Returns:
        str: Rendered HTML template for the home page with the current year.
    """
    current_year = datetime.now().year
    return render_template(template_name_or_list='home.html', current_year=current_year)


if __name__ == "__main__":
    app.run()
