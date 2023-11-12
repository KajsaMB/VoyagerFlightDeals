import requests
import os
from dotenv import load_dotenv
load_dotenv("local.env")

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.sheet_data = {}
        self.endpoint = os.getenv("SHEET_ENDPOINT")
        self.token = {"Authorization": f"Bearer {os.getenv('BEARER_TOKEN')}"}

    def get_sheet(self):
        response = requests.get(url=self.endpoint, headers=self.token)
        response.raise_for_status()
        data = response.json()
        self.sheet_data = data["flightDeal"]
        return self.sheet_data

    def add_destination(self, destination_city, iata_code, price):
        new_destination = {
            "flightdeal": {
                "city": destination_city,
                "iataCode": iata_code,
                "lowestPrice": price,
            }
        }
        response = requests.post(url=f"{self.endpoint}", json=new_destination, headers=self.token)
        print(response.text)

    # def add_iata_code(self):
    #     for city in self.sheet_data:
    #         new_data = {
    #             "flightdeal": {
    #                 "iataCode": city["iataCode"]
    #             }
    #         }
    #         response = requests.put(url=f"{self.endpoint}/{city['id']}", json=new_data, headers=self.token)
    #         print(response.text)

