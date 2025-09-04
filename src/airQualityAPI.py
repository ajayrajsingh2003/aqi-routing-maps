# To check if AirQuality API is working!!! (Used in code with 'allAPI' file)
import requests

# API endpoint
url = "https://atlas.microsoft.com/weather/airQuality/current/json"

# Define your subscription key
subscription_key = "4jGR7GmcVhq38yiuFFUcmOeEHIg4tWNCCKKygbQu2waC0CnhUYbkJQQJ99ALACYeBjFMrplqAAAgAZMP20db"

# Set up parameters including the API version and location query (latitude, longitude)
params = {
    'api-version': '1.1',
    'query': '47.632346,-122.13887',  # Example coordinates for Redmond, WA
    'subscription-key': subscription_key
}

# Make the GET request
response = requests.get(url, params=params)

# Check the response status and data
if response.status_code == 200:
    aqi_data = response.json()
    print(aqi_data)
else:
    print(f"Error {response.status_code}: {response.text}")
