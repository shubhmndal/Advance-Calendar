
import calendar

festivals = {
    (1, 1): "New Year's Day",
    (2, 14): "Valentine's Day",
    (3, 17): "St. Patrick's Day",
    (4, 22): "Earth Day",
    (5, 1): "May Day",
    (6, 21): "Summer Solstice",
    (7, 4): "Independence Day (USA)",
    (8, 15): "Independence Day (India)",
    (9, 21): "World Peace Day",
    (10, 31): "Halloween",
    (11, 11): "Veterans Day",
    (12, 25): "Christmas Day",
}

def add_festivals_to_calendar(year):
    # Create a TextCalendar object
    cal = calendar.TextCalendar(calendar.SUNDAY)

    # Iterate through each month
    for month in range(1, 13):
        # Print the month and year
        print(cal.formatmonth(year, month))

        # Check if any festivals are in this month
        for (fest_month, fest_day), festival_name in festivals.items():
            if fest_month == month:
                # Print the festival details
                print(f"Festival: {festival_name} on {month}/{fest_day}/{year}")
        print("\n")

# Example us
year = 2025
add_festivals_to_calendar(year)


