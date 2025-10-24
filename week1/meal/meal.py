# meal.py

def main():
    # Prompt user for time
    time_input = input("Time: ")
    hours = convert(time_input)

    # Determine which meal it is
    if 7 <= hours <= 8:
        print("breakfast time")
    elif 12 <= hours <= 13:
        print("lunch time")
    elif 18 <= hours <= 19:
        print("dinner time")
    # Otherwise, do nothing


def convert(time):
    """
    Converts a string in 24-hour format '#:##' or '##:##' to float hours.
    Example: '7:30' -> 7.5
    """
    hour_str, minute_str = time.split(":")
    hour = int(hour_str)
    minute = int(minute_str)
    return hour + minute / 60


if __name__ == "__main__":
    main()
