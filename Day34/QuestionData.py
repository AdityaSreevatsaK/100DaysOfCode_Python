import requests

trivia_parameters = {
    "amount": 10,
    "type": "boolean"
}
question_data = requests.get(url="https://opentdb.com/api.php", params=trivia_parameters)
question_data.raise_for_status()
question_data = question_data.json()["results"]
