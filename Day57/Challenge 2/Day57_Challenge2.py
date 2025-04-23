from datetime import datetime

import requests
from flask import Flask, render_template

app = Flask(__name__)

genderize_url = "https://api.genderize.io"
agify_url = "https://api.agify.io"

print("Day 57 - 100 Days of Code.")
print("Welcome to Age and Gender Guesser Based on Name.")


@app.route('/')
def home():
    """
    Renders the home page.

    Returns:
        str: Rendered HTML template for the home page with the current year.
    """
    current_year = datetime.now().year
    return render_template(template_name_or_list='home.html', current_year=current_year)


def get_age(name: str):
    """
    Fetches the predicted age for a given name using the Agify API.

    Args:
        name (str): The name for which to predict the age.

    Returns:
        int: Predicted age for the given name.
    """
    agify_response: dict = requests.get(agify_url + "?name=" + name).json()
    age = agify_response.get('age')
    return age


def get_gender_and_probability(name):
    """
    Fetches the predicted gender and its probability for a given name using the Genderize API.

    Args:
        name (str): The name for which to predict the gender.

    Returns:
        tuple: A tuple containing the predicted gender (str) and its probability (float, as a percentage).
    """
    genderize_response: dict = requests.get(genderize_url + "?name=" + name).json()
    gender = genderize_response.get('gender')
    probability = genderize_response.get('probability') * 100
    return gender, probability


@app.route("/guess/<string:name>")
def guess_age_and_gender(name: str):
    """
    Renders a page with the predicted age and gender for a given name.

    Args:
        name (str): The name for which to predict age and gender.

    Returns:
        str: Rendered HTML template with the name, predicted age, gender, probability, and current year.
    """
    current_year = datetime.now().year
    age = get_age(name)
    gender, probability = get_gender_and_probability(name)
    return render_template(template_name_or_list='guess.html', name=name.title(), age=age, gender=gender,
                           probability=probability, current_year=current_year)


if __name__ == "__main__":
    app.run()
