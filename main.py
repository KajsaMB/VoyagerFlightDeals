from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from datetime import datetime, timedelta
import requests
import os
from dotenv import load_dotenv
import pandas

load_dotenv("local.env")

dm = DataManager()
sheet_data = dm.get_sheet()
flight_search = FlightSearch()
notification_manager = NotificationManager()

HEADERS = {
    "Authorization": f"Bearer {os.getenv('BEARER_TOKEN')}"
}

register_new_users = True
# while register_new_users:
#     reg_complete = False
#     print("Welcome to the Voyager's Flight Club.")
#     print("We find the cheapest flight deals and notify you by email.")
#     new_user = input("Ready to join the club? (Y or N):\n").title()
#
#     if new_user == "Y":
#         first_name = input("Tell us your first name?\n").title()
#         last_name = input("Your last name?\n").title()
#         email = input("And your email?\n")
#         verify_email = input("Verify your email:\n")
#
#         while not reg_complete:
#             if verify_email == email:
#                 print(f"{first_name}, you're in!")
#                 new_user = {
#                     "user": {
#                         "firstName": first_name,
#                         "lastName": last_name,
#                         "email": email,
#                     }
#                 }
#                 response = requests.post(url=f"https://api.sheety.co/9d57a838d5ddf3fa43e5b8042a0cda90/flightDeals/users",
#                                         json=new_user, headers=HEADERS)
#                 response.raise_for_status()
#                 print(response.text)
#                 reg_complete = True
#             else:
#                 print("The email doesn't match.")
#                 verify_email = input("Verify your email again:\n")
#     else:
#         print("Maybe next time!")
#         register_new_users = False

destination_city = input("Would you like to add a new destination? Please enter name of city: ")
add_city = True

if destination_city == "" or "no":
    pass
else:
    for row in sheet_data:
        if destination_city in row['city']:
            add_city = False
    if add_city:
        price = int(input("Max price willing to pay: €"))
        iata_code = flight_search.find_location(destination_city)
        dm.add_destination(destination_city, iata_code, price)
    else:
        print("Destination already exist")

tomorrow = datetime.now() + timedelta(days=1)
date_from = tomorrow.date().strftime("%d" + "/" + "%m" + "/" + "%Y")
six_months = tomorrow + timedelta(weeks=26)
date_to = six_months.date().strftime("%d" + "/" + "%m" + "/" + "%Y")

for destination in sheet_data:
    flight = flight_search.find_flight('DUB', destination['iataCode'], date_from, date_to)
    if flight.price < destination['lowestPrice']:
        print(f"{flight.arrival_city}, €{flight.price}")
        notification_manager.send_notification(flight.departure_airport_code, flight.arrival_city, flight.arrival_airport_code, flight.price, flight.departure_date, flight.return_date)
