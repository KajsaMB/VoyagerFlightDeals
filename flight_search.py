import requests
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta
from flight_data import FlightData
from data_manager import DataManager

data_manager = DataManager()

load_dotenv("local.env")
class FlightSearch:
    # Uses the Flight Search API
    def __init__(self):
        self.location_endpoint = os.getenv("LOCATION_ENDPOINT")
        self.search_endpoint = os.getenv("SEARCH_ENDPOINT")
        self.headers = {"apikey": os.getenv("FLIGHT_KEY")}

    def find_location(self, city_name):
        parameters = {"term": city_name, "location_types": "city"}
        response = requests.get(url=self.location_endpoint, params=parameters, headers=self.headers)
        response.raise_for_status()
        location_data = response.json()["locations"]
        iata_code = location_data[0]["code"]
        return iata_code

    def find_flight(self, departure_code, destination_code, date_from, date_to):
            parameters = {
                "fly_from": departure_code,
                "fly_to": destination_code,
                "date_from": date_from,
                "date_to": date_to,
                "nights_in_dst_from": 7,
                "nights_in_dst_to": 28,
                "flight_type": "round",
                "curr": "EUR",
                "one for city": 1,
                "max_stopovers": 2,
            }
            response = requests.get(url=self.search_endpoint, params=parameters, headers=self.headers)
            response.raise_for_status()
            try:
                data = response.json()["data"][0]
            except IndexError:
                print(f"No flights found for {destination_code}")
                return None

            flight_data = FlightData(price=data["price"], dpt_airport_code=data["flyFrom"], dpt_city=data["cityFrom"], arr_airport_code=data["flyTo"], arr_city=data["cityTo"], dpt_date=data["route"][0]["local_departure"].split("T")[0], return_date=data["route"][1]["local_departure"].split("T")[0])
            return flight_data

