"""
Fetch Weather facts from external provider and return data
"""

import os
import requests
import json
from dotenv import load_dotenv


def get_weather():
    load_dotenv()

    api_key = os.getenv("WEATHERAPI_KEY")
    location = os.getenv("LOCATION")

    if not api_key or not location:
        raise RuntimeError("Missing WEATHERAPI_KEY or LOCATION")

    url = "https://api.weatherapi.com/v1/forecast.json"

    response = requests.get(
        url,
        params={
            "key": api_key,
            "q": location,
        },
        timeout=10,
    )

    data = response.json()

    return {
        "location": f"{data['location']['name']}, {data['location']['region']}",
        "local_time": data["location"]["localtime"],
        "current_temp_c": data["current"]["temp_c"],
        "condition": data["current"]["condition"]["text"],
        "high_temp_c": data["forecast"]["forecastday"][0]["day"]["maxtemp_c"],
        "low_temp_c": data["forecast"]["forecastday"][0]["day"]["mintemp_c"],
    }
