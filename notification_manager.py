import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv("local.env")


class NotificationManager:
    # Sends notifications with the flight details.
    def __init__(self):
        self.client = Client(os.getenv("TWILIO_ACCOUNT_SID"), os.getenv("TWILIO_TOKEN"))
        self.sender = os.getenv("SENDER")
        self.receiver = os.getenv("RECIPIENT")

    def send_notification(self, dpt_airport_code, arr_city, arr_airport_code, price, dpt_date, return_date):
        message = self.client.messages.create(
            body=f"Cheap flight alert! Only €{price} to fly from {dpt_airport_code} to {arr_city}-{arr_airport_code} from {dpt_date} to {return_date}",
            from_=self.sender,
            to=self.receiver,
        )
        print(message.status)
