
class FlightData:
    # Structures the flight data.
    def __init__(self, price, dpt_airport_code, dpt_city, arr_airport_code, arr_city, dpt_date, return_date):
        self.price = price
        self.departure_airport_code = dpt_airport_code
        self.departure_city = dpt_city
        self.arrival_airport_code = arr_airport_code
        self.arrival_city = arr_city
        self.departure_date = dpt_date
        self.return_date = return_date


