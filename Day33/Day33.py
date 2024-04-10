import smtplib
from datetime import datetime

import requests

my_email = "ask@gmail.com"
my_password = "aaaabbbbccccdddd"

ZERO = 0
ONE = 1
FIVE = 5
CURRENT_TIME = datetime.now()
USER_LATITUDE = 12.971599
USER_LONGITUDE = 77.594566
CURRENT_HOUR = int(str(CURRENT_TIME).split(" ")[ONE][ZERO:2])
user_coordinates = {
    "lat": USER_LATITUDE,
    "lng": USER_LONGITUDE,
    "formatted": ZERO
}

sunrise_sunset_response = requests.get(url="https://api.sunrise-sunset.org/json", params=user_coordinates)
sunrise_sunset_response.raise_for_status()
sunrise_sunset_response = sunrise_sunset_response.json()

sunrise_time = sunrise_sunset_response["results"]["sunrise"]
sunset_time = sunrise_sunset_response["results"]["sunset"]
sunrise_time_hour = int(sunrise_time.split("T")[ONE][ZERO:2])
sunset_time_hour = int(sunset_time.split("T")[ONE][ZERO:2])

iss_current_location_response = requests.get(url="http://api.open-notify.org/iss-now.json")
iss_current_location_response.raise_for_status()
iss_latitude = float(iss_current_location_response.json()["iss_position"]["latitude"])
iss_longitude = float(iss_current_location_response.json()["iss_position"]["longitude"])
is_space_station_above_user = (USER_LATITUDE + FIVE >= iss_latitude >= USER_LATITUDE - FIVE and
                               USER_LONGITUDE + FIVE >= iss_longitude >= USER_LONGITUDE + FIVE)
is_space_station_visible_in_user_location = CURRENT_HOUR > sunset_time_hour or CURRENT_HOUR < sunrise_time_hour

if is_space_station_visible_in_user_location and is_space_station_above_user:
    with smtplib.SMTP("SMTP.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs=my_email,
                            msg="Subject:ISS is right above your location!\n\n"
                                "Go outside and check. The ISS is right above your location! ;)")

else:
    print("It is daytime. The space station will not be visible.")
