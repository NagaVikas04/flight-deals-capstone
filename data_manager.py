# from pprint import pprint
import requests

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/4efb27177f922a915e9763cf39352124/flightDeals/prices"
SHEETY_USERS_ENDPOINT = "https://api.sheety.co/4efb27177f922a915e9763cf39352124/flightDeals/users"

headers_sheety = {
    "YOUR SHEETY AUTHORIZATION CODE"
}


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=headers_sheety)
        data = response.json()
        self.destination_data = data["prices"]
        # pprint(data)
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                                    json=new_data,
                                    headers=headers_sheety
                                    )
            print(response.text)

    def get_customer_emails(self):
        customer_endpoint = SHEETY_USERS_ENDPOINT
        response = requests.get(url=customer_endpoint, headers=headers_sheety)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data
