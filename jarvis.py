# Entry point for JARVIS
import sys
from dotenv import load_dotenv

from modules.weather import get_weather
from modules.weather_briefing import format_weather_briefing


def main():
    load_dotenv()

    if len(sys.argv) < 2:
        return

    command = sys.argv[1].lower()

    if command == "weather":
        weather = get_weather()
        briefing = format_weather_briefing(weather)
        print(briefing)


if __name__ == "__main__":
    main()
