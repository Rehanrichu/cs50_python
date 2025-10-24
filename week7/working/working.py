import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    # Regex pattern to capture times like '9 AM to 5 PM' or '9:00 AM to 5:00 PM'
    pattern = r"^(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)$"
    match = re.match(pattern, s)
    if not match:
        raise ValueError("Invalid format")

    h1, m1, p1, h2, m2, p2 = match.groups()

    # Default minutes to 00 if not provided
    m1 = int(m1) if m1 else 0
    m2 = int(m2) if m2 else 0
    h1 = int(h1)
    h2 = int(h2)

    # Check valid hour and minute ranges
    if not (1 <= h1 <= 12) or not (1 <= h2 <= 12) or not (0 <= m1 < 60) or not (0 <= m2 < 60):
        raise ValueError("Invalid time value")

    # Convert both times to 24-hour format
    start = convert_to_24(h1, m1, p1)
    end = convert_to_24(h2, m2, p2)

    return f"{start} to {end}"


def convert_to_24(hour, minute, period):
    if period == "AM":
        if hour == 12:
            hour = 0
    elif period == "PM":
        if hour != 12:
            hour += 12

    return f"{hour:02}:{minute:02}"


if __name__ == "__main__":
    main()
