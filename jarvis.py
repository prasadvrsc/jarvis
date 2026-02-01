# Entry point for JARVIS

from dotenv import load_dotenv
from modules.weather import get_weather


def main():
    load_dotenv()
    get_weather()
    print("Jarvis Online")


if __name__ == "__main__":
    main()
