# Codsoft Task-4
# ______________

import urllib.request
import json

# API key from OpenWeatherMap Website
# ___________________________________

API_KEY = '6f7b0b6afb47c5f5fa57430d47898255' 

def get_weather_data(city_name):
    # Construct the API URL
    # _____________________
    base_url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': city_name,
        'appid': API_KEY,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }

    # Encode the parameters and create the URL
    url = base_url + '?' + urllib.parse.urlencode(params)

    try:
        # Send the API request and retrieve the response
        # ______________________________________________
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode('utf-8'))
        return data
    except urllib.error.HTTPError as e:
        print(f"\nError: Unable to retrieve weather data. Status code {e.code} \n")
        return None

def display_weather(weather_data):
    if weather_data is not None:
        temperature = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        wind_speed = weather_data['wind']['speed']
        status = weather_data['weather'][0]['description']

        print(f"\t\t\t\t\t\t\t\t-> Temperature: {temperature}°C")
        print(f"\t\t\t\t\t\t\t\t-> Humidity: {humidity}%")
        print(f"\t\t\t\t\t\t\t\t-> Wind Speed: {wind_speed} m/s")
        print(f"\t\t\t\t\t\t\t\t-> Description: {status.capitalize()}")
    else:
        print("\n\t\t\t\t\t\t\t\tWeather data not available :(")

if __name__ == "__main__":
    city = input("\nEnter the name of a city or a zip code: ")
    weather_data = get_weather_data(city)

    if weather_data:
        print("\n\t\t\t\t\t\t\t\t  Weather Information for", city,":\n\t\t\t\t\t\t\t\t====================================\n")
        display_weather(weather_data)
