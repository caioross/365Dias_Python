import requests

def get_weather(city_name, api_key):
    """
    Fetches the current weather for a given city using OpenWeatherMap API.

    Args:
        city_name (str): The name of the city.
        api_key (str): The API key for OpenWeatherMap.

    Returns:
        dict: A dictionary containing the weather information.
    """
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

def main():
    """
    Main function to execute the script.
    """
    api_key = 'your_api_key_here'  # Replace with your actual OpenWeatherMap API key
    city_name = input("Enter the city name: ")
    try:
        weather_data = get_weather(city_name, api_key)
        print(f"Weather in {city_name}:")
        print(f"Temperature: {weather_data['main']['temp']}°C")
        print(f"Weather: {weather_data['weather'][0]['description']}")
        print(f"Humidity: {weather_data['main']['humidity']}%")
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")

if __name__ == '__main__':
    main()