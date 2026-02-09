from skills.weather import get_weather
from skills.milestones import upcoming_milestones
from formatters.weather_formatter import format_weather_briefing


def _parse_days(args, default=7) -> int:
    if "--days" not in args:
        return default

    i = args.index("--days")
    if i + 1 >= len(args):
        raise ValueError("Missing value for --days")

    days = int(args[i + 1])
    if days <= 0:
        raise ValueError("--days must be > 0")

    return days


def run_briefing(args) -> None:
    days = _parse_days(args, default=7)

    weather = get_weather()
    weather_text = format_weather_briefing(weather)
    items = upcoming_milestones(days)

    print("📋 Daily Briefing\n")
    print(weather_text)
    print("")

    if items:
        print(f"🎉 Upcoming milestones (next {days} days):")
        for item in items:
            print(
                f"- {item['days_until']}d: {item['name']} - {item['type']} ({item['date']})"
            )
    else:
        print(f"No upcoming milestones in the next {days} days.")
