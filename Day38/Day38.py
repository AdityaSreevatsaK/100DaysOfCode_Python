from datetime import datetime as dt

import requests
from requests.auth import HTTPBasicAuth

# Can be obtained here: https://www.nutritionix.com/business/api
nutritionix_api_key = "376078307a2e0014930d0cd28e8a261b"
application_id = "ad49bfac"
nutritionix_exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
nutritionix_request_headers = {
    "x-app-id": application_id,
    "x-app-key": nutritionix_api_key
}

# Can be obtained here: https://sheety.co/
sheety_post_endpoint = "https://api.sheety.co/ef79f587d7ca4a29986511899e0f2922/myWorkouts/workouts"
sheety_authentication = HTTPBasicAuth('Riptide', '376078307a2e0014930d0cd28e8a261b')
sheet_name = "workout"
headers = {'Content-Type': 'application/json'}

ZERO = 0
weight = ZERO
height = ZERO
age = ZERO

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
        age = 40

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
    sheety_response.raise_for_status()
    print(sheety_response.text)
