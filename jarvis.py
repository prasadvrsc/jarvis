# Entry point for JARVIS
import sys
from dotenv import load_dotenv

from skills.weather import get_weather
from skills.milestones import add_milestone, delete_milestone, upcoming_milestones
from formatters.weather_formatter import format_weather_briefing


def main():
    load_dotenv()

    if len(sys.argv) < 2:
        return

    command = sys.argv[1].lower()

    if command == "weather":
        weather = get_weather()
        briefing = format_weather_briefing(weather)
        print(briefing)
    elif command == "milestone":
        if len(sys.argv) < 3:
            print("Usage:")
            print('  python jarvis.py milestone add <type> "<name>" <YYYY-MM-DD>')
            print('  python jarvis.py milestone delete <type> "<name>"')
            print("  python jarvis.py milestone upcoming <days>")
            return

        action = sys.argv[2].lower()

        if action == "add":
            if len(sys.argv) < 6:
                print(
                    'Usage: python jarvis.py milestone add <type> "<name>" <YYYY-MM-DD>'
                )
                return
            milestone_type = sys.argv[3].lower()
            name = sys.argv[4]
            iso_date = sys.argv[5]
            add_milestone(milestone_type, name, iso_date)
            return

        if action == "delete":
            if len(sys.argv) < 5:
                print('Usage: python jarvis.py milestone delete <type> "<name>"')
                return
            milestone_type = sys.argv[3].lower()
            name = sys.argv[4]
            delete_milestone(milestone_type, name)
            return

        if action == "upcoming":
            if len(sys.argv) < 4:
                print("Usage: python jarvis.py milestone upcoming <days>")
                return
            days = int(sys.argv[3])
            items = upcoming_milestones(days)
            if not items:
                print(f"No milestones in the next {days} days.")
                return
            for item in items:
                print(
                    f'{item["days_until"]}d: {item["name"]} — {item["type"]} ({item["date"]})'
                )
            return

    print(f"Unknown milestone action: {action}")
    return


if __name__ == "__main__":
    main()
