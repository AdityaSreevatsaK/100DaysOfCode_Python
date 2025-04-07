import requests

# Can be obtained here: https://sheety.co/
sheety_prices_get_endpoint = "https://api.sheety.co/" + "************" + "/flightDeals/prices/"


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        """
            Method to obtain the destination data.
        """
        response = requests.get(url=sheety_prices_get_endpoint)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        """
            Method to update the destination data.
        """
        for city in self.destination_data:
            new_data = {
                "price": {
                    "code": city["code"]
                }
            }
            response = requests.put(url=f"{sheety_prices_get_endpoint}/{city['id']}", json=new_data)
            print(response.text)
