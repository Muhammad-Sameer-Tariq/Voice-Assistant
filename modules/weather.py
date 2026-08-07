import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")



def get_weather(city):

    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(url, params=params)

    print("STATUS:", response.status_code)

    if response.status_code != 200:
        return "I couldn't find the weather for that city."

    data = response.json()

    temperature = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    description = data["weather"][0]["description"]
    humidity = data["main"]["humidity"]

    return (
        f"The weather in {city} is {description}. "
        f"The temperature is {temperature} degrees Celsius. "
        f"It feels like {feels_like} degrees. "
        f"Humidity is {humidity} percent."
    )
