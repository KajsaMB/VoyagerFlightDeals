# VoyagerFlightDeals
Finds cheapest flights to user-specified destinations and sends SMS notification if price is below user-specified amount. 
SMS includes info on flight and link to book flight. Can specify length of trip, layovers, time of departure/arrival etc in flight search class. 

Built with OOP in python. Uses Kiwi api to search and find flights, requires location and search endpoint URLs as well as API key. 

Uses Sheety and Sheety api to keep track of desired destinations, users and flights. Requires sheet endpoint URL as well as bearer token.

Uses Twilio to send and recieve SMS notifications. Requires Twilio account sid, token, sender nr, receiver nr.

More improvements, including UI, to come.
