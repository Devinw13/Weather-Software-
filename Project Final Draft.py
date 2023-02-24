import requests

# API key for OpenWeatherMap
api_key = 'f7dd3f81e2ee10712a481e5d2eca6ec1'

def get_weather_data(location):
    """
    Get weather forecast data from OpenWeatherMap API
    :param location: user-input location (zip code or city name)
    :return: weather forecast data in json format
    """
    try:
        # Build the URL for the API request
        url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}'

        # Send the API request and get the response
        response = requests.get(url)

        # Parse the response as JSON
        data = response.json()
        return data
    except:
        print("Error in connecting to OpenWeatherMap API")
        return None

def display_weather_data(data, location):
    """
    Display weather forecast data in a readable format
    :param data: weather forecast data in json format
    """
    if data:
        # Extract the relevant information from the response
        temp = data['main']['temp']
        temp_min = data['main']['temp_min']
        temp_max = data['main']['temp_max']
        weather = data['weather'][0]['main']

        # Print the information in a readable format
        print(f"Current temperature in {location} is {temp} Kelvin")
        print(f"Minimum temperature in {location} is {temp_min} Kelvin")
        print(f"Maximum temperature in {location} is {temp_max} Kelvin")
        print(f"Weather in {location} is {weather} ")
    else:
        print("Invalid location or unable to connect to OpenWeatherMap API")

def main():
    """
    Main function to get location from user, get weather forecast data and display it
    """
    while True:
        location = input("Enter your zip code or city name (or 'q' to quit): ")
        if location == 'q':
            break
        
        if not location.isalpha() and not location.isdigit():
            print("Invalid input, please enter a valid zip code or city name.")
            continue

        data = get_weather_data(location)
        display_weather_data(data, location)

    print("Exiting program.")

if __name__ == '__main__':
    main()
