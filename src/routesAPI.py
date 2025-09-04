# To check if routes API is working!!! (Used in code with 'allAPI' file)

import requests

# Azure Maps Route API endpoint
url = "https://atlas.microsoft.com/route/directions/json"

# Your Azure Maps subscription key
subscription_key = "EdwQ2SrpwMoN4HNvOkVQFKhNZnsQit95xnlu4IZrYfIqtxdzuTkGJQQJ99AIACYeBjFMrplqAAAgAZMPIzPC"

# Define query parameters
params = {
    'subscription-key': subscription_key,
    'api-version': '1.0',
    'query': '47.6739881,-122.121512:47.6149,-122.1941',  # Coordinates of the start and end points
    'travelMode': 'car',  # Optional: driving, walking, etc.
    #'maxAlternatives': '1'
}

# Make the API request
response = requests.get(url, params=params)

# Check the response
if response.status_code == 200:
    route_data = response.json()
    print(route_data)
else:
    print(f"Error {response.status_code}: {response.text}")

