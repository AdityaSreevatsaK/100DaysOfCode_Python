from datetime import datetime, timedelta

import FlightSearch
import NotificationManager
from DataManager import DataManager

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()

start_city = 'ABC'

print("Day 40 - 100 Days of Code.")
print("Welcome to Flight Club.")

if sheet_data[0]['iataCode'] == '':
    city_names = [row['city'] for row in sheet_data]
    data_manager.city_codes = FlightSearch.get_destination_code(city_names)
    data_manager.update_destination_codes()
    sheet_data = data_manager.get_destination_data()

destinations = {
    data['iataCode']: {
        'id': data['id'],
        'city': data['city'],
        'price': data['lowestPrice']
    } for data in sheet_data}

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=6 * 30)

for destination_code in destinations:
    flight = FlightSearch.check_flights(
        start_city,
        destination_code,
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    print(flight.price)
    if flight is None:
        continue

    if flight.price < destinations[destination_code]['price']:

        users = data_manager.get_customer_email()
        emails = [row['email'] for row in users]
        names = [row['firstName'] for row in users]

        message = (f'Low price alert! Only £{flight.price} to fly from {flight.origin_city} - {flight.origin_airport} '
                   f'to {flight.destination_city}-{flight.destination_airport}, '
                   f'from {flight.out_date} to {flight.return_date}.')

        if flight.stop_overs > 0:
            message += f'\nFlight has {flight.stop_overs} stop over, via {flight.via_city}.'

        link = (f'https://www.google.co.uk/flights?hl=en#flt='
                f'{flight.origin_airport}.{flight.destination_airport}.{flight.out_date}*{flight.destination_airport}'
                f'.{flight.origin_airport}.{flight.return_date}')

        NotificationManager.send_email(emails, message, link)
