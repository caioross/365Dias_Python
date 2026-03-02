import calendar
from datetime import datetime
import os

def load_holidays():
    """Load holidays from a file if it exists."""
    holidays = {}
    if os.path.exists('holidays.txt'):
        with open('holidays.txt', 'r') as file:
            for line in file:
                date, name = line.strip().split(',')
                holidays[date] = name
    return holidays

def load_events():
    """Load events from a file if it exists."""
    events = {}
    if os.path.exists('events.txt'):
        with open('events.txt', 'r') as file:
            for line in file:
                date, description = line.strip().split(',')
                events[date] = description
    return events

def display_calendar(year, month, holidays, events):
    """Display the calendar for a given month and year with holidays and events."""
    print(calendar.month(year, month))
    cal = calendar.Calendar()
    for day in cal.itermonthdays2(year, month):
        if day[0] != 0:
            date_str = f"{year:04d}-{month:02d}-{day[0]:02d}"
            if date_str in holidays:
                print(f"Holiday: {day[0]:02d} - {holidays[date_str]}")
            if date_str in events:
                print(f"Event: {day[0]:02d} - {events[date_str]}")

def main():
    """Main function to execute the calendar display."""
    today = datetime.today()
    year = today.year
    month = today.month
    holidays = load_holidays()
    events = load_events()
    display_calendar(year, month, holidays, events)

if __name__ == '__main__':
    main()