# All the url are working and giving us required data
def connecting_url():
    # Azure Maps Route API endpoint
    route_url = "https://atlas.microsoft.com/route/directions/json"

    # Azure Maps Weather API endpoint for current conditions
    weather_url= "https://atlas.microsoft.com/weather/currentConditions/json"

    # Azure Maps Air Quality endpoint for current conditions
    air_quality_url = "https://atlas.microsoft.com/weather/airQuality/current/json"

    return route_url, weather_url, air_quality_url