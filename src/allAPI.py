import requests

# Importing all urls for json data
from urls import connecting_url

# Call url file and fetch all urls
all_url = connecting_url()
aqi_url = all_url[2]  # AQI url

# function to check if API is responding
def response_check():
    pass

# Class JSON will create Route, Weather, AQI JSON
class Json:
    def __init__(self, subscription_key, start_coords, end_coords, travel_mode):
        self.subscription_key = subscription_key
        self.start_coords = start_coords
        self.end_coords = end_coords
        self.travel_mode = travel_mode

    # Creating Route Json
    def get_route(self):
        # Define query parameters
        params = {
            'subscription-key': self.subscription_key,
            'api-version': '1.0',
            'query': f'{self.start_coords.replace(" ","")}:{self.end_coords.replace(" ","")}',  # Coordinates of the start and end points
            'travelMode': self.travel_mode,  # Optional: driving, walking, etc.
            'maxAlternatives': '1'
        }
        # Make the API request
        route_url = all_url[0]  # Routing url
        response = requests.get(route_url, params=params)

        # Check the response
        if response.status_code == 200:
            route_data = response.json()
            print(route_data)
        else:
            print(f"Error {response.status_code}: {response.text}")
        return route_data



class AqiData():
    def __init__(self, subscription_key, lat_coord, long_coord):
        self.subscription_key = subscription_key
        self.lat_coord = lat_coord
        self.long_coord = long_coord

    # hitting the AQI API
    def aqi_api(self):
        # Define query parameters
        params = {

            'api-version': '1.0',
            'query': f'{self.lat_coord},{self.long_coord}',
            'subscription-key': self.subscription_key,
        }

        # Make the GET request
        response = requests.get(aqi_url, params=params)

        # Check the response status and data
        if response.status_code == 200:
            aqi_data = response.json()
            print(aqi_data)
        else:
            print(f"Error {response.status_code}: {response.text}")
        return aqi_data
