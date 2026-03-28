import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")

if not API_KEY:
    raise ValueError("API key not found. Please set it in the .env file.")

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=params)

        # Task 2 — Handle errors properly
        if response.status_code == 200:
            data = response.json()
            return data

        elif response.status_code == 401:
            print("Error: Invalid API key.")
        
        elif response.status_code == 429:
            print("Error: Rate limit exceeded. Please try again later.")
        
        else:
            print(f"Error: API request failed with status code {response.status_code}")

    except requests.exceptions.RequestException as e:
        print("Request failed:", e)


if __name__ == "__main__":
    city = input("Enter city name: ")

    # Task 3 — Privacy protection
    # Do NOT log user location data (e.g., city names) to console or logs.
    # This helps comply with privacy principles such as data minimization (GDPR)
    # and protects sensitive user location information.

    weather = get_weather(city)

    if weather:
        print("Temperature:", weather["main"]["temp"], "°C")
        print("Weather:", weather["weather"][0]["description"])
