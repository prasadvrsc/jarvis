"""
Fetch Weather facts from external provider and return data
"""

import os
import requests
import json
from dotenv import load_dotenv


def get_weather():
    print("DEBUG: entered get_weather()")
    load_dotenv()

    api_key = os.getenv("WEATHERAPI_KEY")
    location = os.getenv("LOCATION")

    if not api_key or not location:
        raise RuntimeError("Missing WEATHERAPI_KEY or LOCATION")

    url = "https://api.weatherapi.com/v1/current.json"

    response = requests.get(
        url,
        params={
            "key": api_key,
            "q": location,
        },
        timeout=10,
    )

    print(json.dumps(response.json(), indent=2))
