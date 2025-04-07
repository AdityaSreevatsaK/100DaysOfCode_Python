from datetime import datetime as dt

import requests
from requests.auth import HTTPBasicAuth

# Can be obtained here: https://www.nutritionix.com/business/api
nutritionix_api_key = "************"
application_id = "************"
nutritionix_exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
nutritionix_request_headers = {
    "x-app-id": application_id,
    "x-app-key": nutritionix_api_key
}

# Can be obtained here: https://sheety.co/
sheety_post_endpoint = "https://api.sheety.co/URL/myWorkouts/workouts"
sheety_authentication = HTTPBasicAuth('************', '************')
sheet_name = "workout"
headers = {'Content-Type': 'application/json'}

ZERO = 0
weight = ZERO
height = ZERO
age = ZERO

print("Day 38 - 100 Days of Code.")
print("Welcome to  Workout Tracker using Google Sheets.")

try:
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in centimetres: "))
    age = int(input("Enter your age in years: "))
except Exception as e:
    print(e)
    if weight == ZERO:
        weight = 70
    if height == ZERO:
        height = 170
    if age == ZERO:
        age = 30

nutritionix_parameters = {
    "query": input("Please enter your exercise details for today:\n"),
    "weight_kg": weight,
    "height_cm": height,
    "age": age
}

nutritionix_response = requests.post(url=nutritionix_exercise_endpoint,
                                     headers=nutritionix_request_headers,
                                     json=nutritionix_parameters)
nutritionix_response.raise_for_status()
exercise_details = nutritionix_response.json()["exercises"]

for detail in exercise_details:
    sheety_params = {
        sheet_name: {
            "date": str(dt.now().date()),
            "time": str(dt.now().time())[:8],
            "duration": detail["duration_min"],
            "exercise": detail["name"].title(),
            "calories": detail["nf_calories"]
        }
    }
    sheety_response = requests.post(url=sheety_post_endpoint,
                                    json=sheety_params,
                                    headers=headers,
                                    auth=sheety_authentication)
    try:
        sheety_response.raise_for_status()
    except requests.exceptions.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except requests.exceptions.ConnectionError as conn_err:
        print(f'Connection error occurred: {conn_err}')
    except requests.exceptions.Timeout as timeout_err:
        print(f'Timeout error occurred: {timeout_err}')
    except requests.exceptions.RequestException as req_err:
        print(f'An error occurred: {req_err}')
    else:
        print(sheety_response.text)
        print("Details added successfully.")
