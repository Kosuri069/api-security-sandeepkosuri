# weather.py
import requests
from config import API_KEY

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city):
    """
    Fetch weather data for a given city using OpenWeatherMap API.
    Returns a dictionary with weather info or an 'error' key in case of failure.
    """
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=5)

        # Successful response
        if response.status_code == 200:
            data = response.json()
            # Safely extract fields
            temp = data.get("main", {}).get("temp", "N/A")
            weather_desc = data.get("weather", [{}])[0].get("description", "N/A")
            return {"temp": temp, "description": weather_desc}

        # Unauthorized - API key problem
        elif response.status_code == 401:
            return {"error": "Invalid API key."}

        # Too many requests
        elif response.status_code == 429:
            return {"error": "Rate limit exceeded. Try again later."}

        # City not found
        elif response.status_code == 404:
            return {"error": "City not found."}

        # Other API errors
        else:
            return {"error": f"Unexpected API error: {response.status_code}"}

    except requests.exceptions.RequestException:
        return {"error": "Network error. Please try again later."}


def main():
    city = input("Enter city name: ")

    # Privacy Note:
    # User location data (city names) is not logged to protect privacy.
    # This follows GDPR data minimization principles, as location data
    # can be considered personally identifiable information (PII).

    result = get_weather(city)

    if "error" in result:
        print(result["error"])
    else:
        print(f"Temperature in {city}: {result['temp']} °C")
        print(f"Weather description: {result['description']}")


if __name__ == "__main__":
    main()
