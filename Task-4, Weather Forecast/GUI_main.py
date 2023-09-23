# Codsoft Task-4
# ______________

import tkinter as tk
from tkinter import ttk
import urllib.request
import json

# API key from OpenWeatherMap Website
# ___________________________________
API_KEY = '6f7b0b6afb47c5f5fa57430d47898255'

def get_weather_data(city_name):
    base_url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': city_name,
        'appid': API_KEY,
        'units': 'metric' 
    }
    url = base_url + '?' + urllib.parse.urlencode(params)

    try:
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode('utf-8'))
        return data
    except urllib.error.HTTPError as e:
        return None

def display_weather(weather_data):
    if weather_data is not None:
        temperature = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        wind_speed = weather_data['wind']['speed']
        status = weather_data['weather'][0]['description']

        result_label.config(text=f"Weather Information:\nTemperature: {temperature}°C\nHumidity: {humidity}%\nWind Speed: {wind_speed} m/s\nDescription: {status.capitalize()}")
    else:
        result_label.config(text="Weather data not available :(")

# Function to fetch weather data and display it
# _____________________________________________
def fetch_and_display_weather():
    city = city_entry.get()
    weather_data = get_weather_data(city)
    display_weather(weather_data)

# Create the main GUI window
# __________________________
root = tk.Tk()
root.title("Weather Forecast")

# Create a frame for better styling
# _________________________________
frame = ttk.Frame(root)
frame.pack(padx=20, pady=20)

# Create labels and entry fields
# ______________________________
city_label = ttk.Label(frame, text="Enter city or zip code:")
city_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

city_entry = ttk.Entry(frame)
city_entry.grid(row=0, column=1, padx=5, pady=5)

fetch_button = ttk.Button(frame, text="Fetch Weather", command=fetch_and_display_weather)
fetch_button.grid(row=1, column=0, columnspan=2, padx=5, pady=10)

result_label = ttk.Label(frame, text="")
result_label.grid(row=2, column=0, columnspan=2, pady=10)

# Apply padding and expansion options for widgets
# _______________________________________________
for child in frame.winfo_children():
    child.grid_configure(padx=10, pady=5)
    
frame.columnconfigure((0, 1), weight=1)

# Start the Tkinter main loop
# ___________________________
root.mainloop()
