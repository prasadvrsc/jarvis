from datetime import datetime


def _greeting_from_hour(hour: int) -> str:
    if 5 <= hour < 12:
        return "Good morning"
    if 12 <= hour < 17:
        return "Good afternoon"
    if 17 <= hour < 23:
        return "Good evening"
    return "Good night"


def format_weather_briefing(weather: dict) -> str:
    # Parse local time (already in local timezone)
    local_dt = datetime.strptime(weather["local_time"], "%Y-%m-%d %H:%M")
    greeting = _greeting_from_hour(local_dt.hour)

    return (
        f"{greeting}. "
        f"It's {local_dt.strftime('%I:%M %p')} in {weather['location'].title()}. "
        f"The current temperature is {weather['current_temp_c']}°C with "
        f"{weather['condition'].lower()} conditions. "
        f"Today's high is {weather['high_temp_c']}°C and the low is "
        f"{weather['low_temp_c']}°C."
    )
