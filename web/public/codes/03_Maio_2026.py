import requests
from datetime import datetime

def get_weather_forecast(city, api_key):
    """
    Fetches the weather forecast for the next 3 days for a given city using OpenWeatherMap API.

    Parameters:
    city (str): The name of the city.
    api_key (str): The API key for OpenWeatherMap.

    Returns:
    dict: A dictionary containing the weather forecast for the next 3 days.
    """
    base_url = "http://api.openweathermap.org/data/2.5/forecast"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric',  # Use 'imperial' for Fahrenheit
        'cnt': 8  # Get 3 days of forecast (3 days * 3 hours/forecast)
    }
    
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

def display_forecast(forecast_data):
    """
    Displays the weather forecast for the next 3 days.

    Parameters:
    forecast_data (dict): The weather forecast data.
    """
    print("Weather Forecast for the Next 3 Days:")
    for entry in forecast_data['list']:
        dt = datetime.fromtimestamp(entry['dt'])
        temperature = entry['main']['temp']
        description = entry['weather'][0]['description']
        print(f"{dt.strftime('%Y-%m-%d %H:%M')} - Temp: {temperature}°C - {description.capitalize()}")

def main():
    """
    Main function to execute the weather forecast script.
    """
    city = input("Enter the city name: ")
    api_key = 'your_api_key_here'  # Replace with your actual OpenWeatherMap API key
    try:
        forecast_data = get_weather_forecast(city, api_key)
        display_forecast(forecast_data)
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()