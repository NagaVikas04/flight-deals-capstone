# import requests
# from datetime import datetime, timedelta

kiwi_search_endpoint = "https://api.tequila.kiwi.com/v2/search"
kiwi_api_key = "YOUR KIWI API KEY"


class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self, price, origin_city, origin_airport, destination_city, destination_airport, out_date, return_date):
        self.price = price
        self.origin_city = origin_city
        self.origin_airport = origin_airport
        self.destination_city = destination_city
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date


    # def get_flights_info(self, to_city):
    #     date = datetime.now()
    #     tomorrow_date = date.date() + timedelta(1)
    #     end_date = date.date() + timedelta(180)
    #
    #     search_headers = {
    #         "apikey": kiwi_api_key
    #     }
    #
    #     search_params = {
    #         "fly_from": "LON",
    #         "fly_to": to_city,
    #         "date_from": tomorrow_date,
    #         "date_to": end_date,
    #         "flight_type": "oneway",
    #         "one_per_date": 1,
    #         "curr": "USD"
    #     }
    #
    #     response = requests.get(url=kiwi_search_endpoint, params=search_params, headers=search_headers)
    #     data = response.json()
    #     cheapest_price_of_the_day = data["data"][0]["price"]
    #     departure_date_in_utc = data["data"][0]['utc_departure']
    #     return cheapest_price_of_the_day, departure_date_in_utc



