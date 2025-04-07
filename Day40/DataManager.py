import requests

# Can be obtained here: https://sheety.co/
sheety_prices_endpoint = "https://api.sheety.co/" + "************" + "/flightDeals/prices/"
sheety_users_endpoint = "https://api.sheety.co/" + "************" + "/flightDeals/users/"


class DataManager:

    def __init__(self):
        self.customer_data = None
        self.destination_data = {}

    def get_destination_data(self):
        """
            Method to obtain the destination data.
        """
        response = requests.get(url=sheety_prices_endpoint)
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
            response = requests.put(url=f"{sheety_prices_endpoint}/{city['id']}", json=new_data)
            print(response.text)

    def get_customer_email(self):
        response = requests.get(url=sheety_users_endpoint)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data
