# To check if weather API is working!!! (Used in code with 'allAPI' file)

import requests

# 1. Azure Maps Weather API endpoint for current conditions
url1 = "https://atlas.microsoft.com/weather/currentConditions/json"

# Your Azure Maps subscription key (shared key authentication)
subscription_key = "EdwQ2SrpwMoN4HNvOkVQFKhNZnsQit95xnlu4IZrYfIqtxdzuTkGJQQJ99AIACYeBjFMrplqAAAgAZMPIzPC"

# Define query parameters
params = {
    'subscription-key': subscription_key,
    'api-version': '1.1',
    'query': '40.730610,-73.935242',  # Latitude and longitude of the location (New York)
    'unit': 'metric'  # 'metric' or 'imperial'

}

# Make the API request
response = requests.get(url1, params=params)

# Check the response

print(response)
if response.status_code == 200:
    weather_data = response.json()
    print(weather_data)
else:
    print(f"Error: {response.status_code}")



