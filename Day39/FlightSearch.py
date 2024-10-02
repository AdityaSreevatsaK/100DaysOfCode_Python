import requests

from FlightData import FlightData

# Can be obtained here: https://tequila.kiwi.com/portal/login
tequila_get_endpoint = "https://tequila-api.kiwi.com"
tequila_api_key = "abcdabcdabcdabcd"
ZERO = 0


def get_destination_code(city_name):
    location_endpoint = f"{tequila_get_endpoint}/locations/query"
    headers = {"apikey": tequila_api_key}
    query = {"term": city_name, "location_types": "city"}
    response = requests.get(url=location_endpoint, headers=headers, params=query)
    results = response.json()["locations"]
    code = results[ZERO]["code"]
    return code


def check_flights(origin_city_code, destination_city_code, from_time, to_time):
    headers = {"apikey": tequila_api_key}
    query = {
        "fly_from": origin_city_code,
        "fly_to": destination_city_code,
        "date_from": from_time.strftime("%d/%m/%Y"),
        "date_to": to_time.strftime("%d/%m/%Y"),
        "nights_in_dst_from": 7,
        "nights_in_dst_to": 28,
        "flight_type": "round",
        "one_for_city": 1,
        "max_stopovers": ZERO,
        "curr": "GBP"
    }

    response = requests.get(
        url=f"{tequila_get_endpoint}/v2/search",
        headers=headers,
        params=query,
    )

    try:
        data = response.json()["data"][ZERO]
    except IndexError:
        print(f"No flights found for {destination_city_code}.")
        return None

    route_string = "route"
    flight_data = FlightData(
        price=data["price"],
        origin_city=data[route_string][ZERO]["cityFrom"],
        origin_airport=data[route_string][ZERO]["flyFrom"],
        destination_city=data[route_string][ZERO]["cityTo"],
        destination_airport=data[route_string][ZERO]["flyTo"],
        out_date=data[route_string][ZERO]["local_departure"].split("T")[ZERO],
        return_date=data[route_string][1]["local_departure"].split("T")[ZERO]
    )
    print(f"{flight_data.destination_city}: £{flight_data.price}")
    return flight_data

