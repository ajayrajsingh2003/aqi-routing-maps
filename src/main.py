# offline data used with json format in text file 'route_json_2_alternatives.txt', check line 13 and see dynamic working in line 16-17
import json

from subscriptionKeysAzure import subscription_keys  # Subscription Key
subscription_key = subscription_keys()
from allAPI import Json, AqiData  # Get Route,weather,AQI JSON
from urls import connecting_url  # Get Route,weather,AQI URLS


# Function creating final JSON for Front-end (PATI (Other Developer))
def final_json(subscription_key, start_coords, end_coords, travel_mode):

    # Uncomment line 16-17 if you have azure subscription keys

    # # check class Json and fetch route in dynamic mode (for this you need to have Azure Maps keys)
    # check_route = Json(subscription_key, start_coords, end_coords, travel_mode)
    # route_data = check_route.get_route()

    # Comment out line 23-25 if you are accessing the azure maps keys in real time

    # Offline json text file to read the routes and see the algorithm work
    # Open and read the file
    with open('C:/Users/ajayr/Desktop/Projects For Github/Capstone Code/pythonProject/data/route_json_2_alternatives.txt', 'r') as file:
        file_contents = file.read()
        route_data = json.loads(file_contents)  # Parse the JSON content

    # Coordinate after how many meters must be calculated (500 meters)
    static_length_per_point = 500

    # Dynamic calculation for number of routes
    no_of_routes = len(route_data['routes'])  # two paths


    # Create JSON
    # send to frontend
    json_frontend = {'route_data': {}}
    json_frontend['route_data']['routes'] = {}

    # updating the json for alternate paths
    for route_number in range(no_of_routes):

        # Alternate difference in sent coordinates
        send_coord = 0

        # Calculate avg travel time in meters
        # total route length in meters
        length_in_meters = int(route_data['routes'][route_number]['summary']['lengthInMeters'])

        # total travel time in seconds
        total_travel_time = int(route_data['routes'][route_number]['summary']['travelTimeInSeconds'])

        # average length at which a coordinate is present in meters
        avg_travel_time = length_in_meters / total_travel_time

        # Calculate after how many points we are reaching 500 meters
        no_of_alternate_coord = static_length_per_point / avg_travel_time

        # Total number of points available at route (latitude and longitude)
        total_no_of_points = len(route_data['routes'][route_number]['legs'][0]['points'])

        # total number of points taken in consideration
        avg_coord_points = int(total_no_of_points / no_of_alternate_coord)

        # Update Json for different paths
        json_frontend['route_data']['routes'][route_number] = [{}]
        json_frontend['route_data']['routes'][route_number][0]['legs'] = {}
        json_frontend['route_data']['routes'][route_number][0]['legs']['points'] = []


        # traversing on exact avg points (latitude and longitude)
        coord_num = 0
        lat_long_point = 0
        while coord_num <= avg_coord_points:

            # extract the lat and long from the route json
            exact_coord = route_data['routes'][route_number]['legs'][0]['points'][lat_long_point]

            # add the extracted lat and long to frontend json
            json_frontend['route_data']['routes'][route_number][0]['legs']['points'].append(exact_coord)

            # increment in index of lat and long coming from route json
            lat_long_point += int(no_of_alternate_coord-1)

            coord_num += 1

        # adding last index to json
        exact_coord = route_data['routes'][route_number]['legs'][0]['points'][total_no_of_points-1]
        json_frontend['route_data']['routes'][route_number][0]['legs']['points'].append(exact_coord)

    # At the end return complete front_end json for latitude and longitude
    return json_frontend

# Create Aqi for frontend
def json_aqi(route_points):

    # Dynamic calculation for number of routes
    no_of_routes = len(route_points['route_data']['routes'])  # two paths

    # Loop to create aqi data for a path --> with the help of lat and long points
    for route_number in range(no_of_routes):

        # Number of latitude and longitude pair in a path
        no_lat_long_pair = len(route_points['route_data']['routes'][route_number][0]['legs']['points'])

        pair_num = 0
        # Call Aqi Api on each pair
        while pair_num < no_lat_long_pair:

            # Fetch out latitude
            lat_on_route = str(route_points['route_data']['routes'][route_number][0]['legs']['points'][pair_num]['latitude'])
            # Fetch out longitude
            long_on_route = str(route_points['route_data']['routes'][route_number][0]['legs']['points'][pair_num]['longitude'])

            # Call AQI API on each pair
            check_aqi = AqiData(subscription_key, lat_on_route,long_on_route)
            route_point_api = check_aqi.aqi_api()
            # Save the AQI in a list and return it
            # IF YOU HAVE REACHED THIS POINT, IT MEANS YOU HAVE READ THE CODE WELL. HOW ABOUT WE CONNECT AND DISCUSS THE PROJECT!!!!!!!!

# main script
if __name__ == "__main__":

    # Call the function to get the subscription key
    subscription_key = subscription_keys()  # Calling the function to get the key

    # Temporarily using these 3 inputs which will be dynamic if you have Access to Azure keys

    # Starting Point
    start_coords = "47.6739881, -122.121512"

    # Destination Point or End Point
    end_coords = "47.6149,-122.1941"

    # What is the Mode of Travel
    travel_mode = "car"

    # Calling final_json function to create JSON file for front-end
    final_route_points = final_json(subscription_key, start_coords, end_coords, travel_mode)

    # Access AQI points only when you have access to Azure keys # I HAVE KEPT ALGORITHM OFFLINE AS THE RESEARCH PAPER IS UNDER REVIEW @NJBDA.....
    json_aqi = json_aqi(final_route_points)

    # What about weather data, CHECK THE VIDEO EXPLANATION OR RESEARCH PAPER, AND REACH OUT TO ME FOR A BETTER UNDERSTANDING OF THIS PROJECT!!!!!