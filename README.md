# Advanced Calendar 

This is an advanced Python project that generates a calendar for a given year and highlights holidays. It uses Python's built-in `calendar` module and a custom list of holidays to display a comprehensive calendar with special dates marked.

---

## **Features**
- Displays a text-based calendar for a specified year.
- Highlights holidays and special dates.
- Easy to customize and extend with additional holidays or events.
- Lightweight and no external dependencies.

---

## **Requirements**
- Python 3.x

---

## **Installation**
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/advanced-calendar.git
   ```
2. Navigate to the project directory:
   ```bash
   cd advanced-calendar
   ```

---

## **Usage**
1. Run the script:
   ```bash
   python advanced_calendar.py
   ```
2. Enter the year when prompted:
   ```
   Enter the year: 2025
   ```
3. The script will display the calendar for the specified year with holidays marked.

---

## **Example Output**
```
    January 2025
Su Mo Tu We Th Fr Sa
 1  2  3  4  5  6  7
 8  9 10 11 12 13 14
15 16 17 18 19 20 21
22 23 24 25 26 27 28
29 30 31

Holidays:
- January 1: New Year's Day
- January 26: Republic Day (India)
```

---

## **Customization**
- Add or modify holidays in the `holidays` dictionary in the script:
  ```python
  holidays = {
      (1, 1): "New Year's Day",
      (1, 26): "Republic Day (India)",
      (12, 25): "Christmas Day",
      # Add more holidays here
  }
  ```
- Change the starting day of the week (e.g., Monday instead of Sunday):
  ```python
  cal = calendar.TextCalendar(calendar.MONDAY)
  ```

---


## **Contact**
For questions or feedback, please reach out to:
- Shubh Mandal
- GitHub: [shubhmndal](https://github.com/shubhmndal)

---

Enjoy using the Advanced Calendar with Holidays! 🎉
