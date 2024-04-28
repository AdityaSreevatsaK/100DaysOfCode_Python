import smtplib

import requests

my_email = "ask@gmail.com"
my_password = "aaaabbbbccccdddd"

take_an_umbrella_email = ("Subject:It's going to rain today!\n\n"
                          "Hey, its going to be raining today. Take an umbrella with you. :)")

will_rain = False
USER_LATITUDE = 12.971599
USER_LONGITUDE = 77.594566
API_KEY = "ay5d634fdfe568dr8u395f8f0p0e09d4o1"
weather_data_parameters = {
    "lat": USER_LATITUDE,
    "lon": USER_LONGITUDE,
    "appid": API_KEY,
    "units": "metric",
    "cnt": 4
}

weather_data = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=weather_data_parameters)
weather_data.raise_for_status()
weather_data = weather_data.json()["list"]
weather_condition = []
for iterator in range(4):
    if weather_data[iterator]["weather"][0]["id"] in range(200, 540):
        will_rain = True
    else:
        pass

if will_rain:
    with smtplib.SMTP("SMTP.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=take_an_umbrella_email)
