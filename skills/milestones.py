"""
python jarvis.py milestone add birthday "John" 1990-05-14
python jarvis.py milestone delete birthday "John"
python jarvis.py milestone upcoming 30
"""

import json
from pathlib import Path
from datetime import date, datetime, timedelta

DATA_FILE = Path("data/contacts.json")


def _load_contacts() -> dict:
    """Load contacts data from disk."""
    if not DATA_FILE.exists():
        return {"people": {}}

    content = DATA_FILE.read_text().strip()
    if not content:
        return {"people": {}}

    try:
        return json.loads(content)
    except json.JSONDecodeError:
        # Returning an empty list is safer than crashing the whole app
        return {"people": {}}


def _save_contacts(data: dict) -> None:
    """Write contacts data to disk."""
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    DATA_FILE.write_text(json.dumps(data, indent=4))


def add_milestone(milestone_type: str, person_name: str, date_iso: str) -> None:
    """Add or update a milestone for a person."""
    data = _load_contacts()
    people = data.setdefault("people", {})

    person = people.setdefault(person_name, {})
    milestones = person.setdefault("milestones", {})

    is_update = milestone_type in milestones
    milestones[milestone_type] = date_iso

    _save_contacts(data)

    action = "Updated" if is_update else "Added"
    print(f"{action} {person_name}: {milestone_type} = {date_iso}")


def delete_milestone(milestone_type: str, person_name: str) -> None:
    """Delete a milestone for a person."""
    data = _load_contacts()
    people = data.get("people", {})

    person = people.get(person_name)
    if not person:
        print(f'No entry found for "{person_name}".')
        return

    milestones = person.get("milestones", {})
    if milestone_type not in milestones:
        print(f'No "{milestone_type}" milestone found for "{person_name}".')
        return

    del milestones[milestone_type]

    # Optional cleanup: remove person if no milestones left
    if not milestones:
        del people[person_name]

    _save_contacts(data)
    print(f"Deleted {person_name}: {milestone_type}")


def upcoming_milestones(days: int) -> list[dict]:
    """Returns milestones occurring in the next N days (inclusive).
    Args:
        days: The number of days from today to look forward.
    Returns:
        A list of dictionaries containing milestone details, sorted by date.
    """
    data = _load_contacts()
    people = data.get("people", {})
    today = date.today()
    results: list[dict] = []

    for person_name, person in people.items():
        milestones = person.get("milestones", {})
        for milestone_type, stored_iso_date in milestones.items():
            milestone_date = date.fromisoformat(stored_iso_date)
            next_occurrence = date(today.year, milestone_date.month, milestone_date.day)
            if next_occurrence < today:
                next_occurrence = date(
                    today.year + 1, milestone_date.month, milestone_date.day
                )
            days_until = (next_occurrence - today).days
            if 0 <= days_until <= days:
                results.append(
                    {
                        "name": person_name,
                        "type": milestone_type,
                        "date": next_occurrence.isoformat(),
                        "days_until": days_until,
                    }
                )
    results.sort(key=lambda x: x["days_until"])
    return results
