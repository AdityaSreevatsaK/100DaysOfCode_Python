from datetime import datetime, timedelta

import FlightSearch
from DataManager import DataManager
from NotificationManager import NotificationManager

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
notification_manager = NotificationManager()

start_city = "ABC"

if sheet_data[0]["code"] == "":
    for row in sheet_data:
        row["code"] = FlightSearch.get_destination_code(row["city"])
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    flight = FlightSearch.check_flights(
        start_city,
        destination["code"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    if flight.price < destination["lowestPrice"]:
        notification_manager.send_sms(message=f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-"
                                              f"{flight.origin_airport} to {flight.destination_city}-"
                                              f"{flight.destination_airport}, from {flight.out_date} to "
                                              f"{flight.return_date}."
                                      )
