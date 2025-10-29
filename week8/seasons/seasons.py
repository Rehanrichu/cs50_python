from datetime import date
import inflect
import sys


def main():
    birth_str = input("Date of Birth: ")
    try:
        year, month, day = map(int, birth_str.split("-"))
        birth_date = date(year, month, day)
    except ValueError:
        sys.exit("Invalid date")

    print(minutes_to_words(birth_date))

def minutes_to_words(birth_date):
    today = date.today()
    difference = today - birth_date
    minutes = difference.days * 24 * 60

    p = inflect.engine()
    # group=1 adds commas between thousands (e.g., 527,040)
    words = p.number_to_words(minutes, andword="", group=1)
    words = words.capitalize() + " minutes"

    return words


if __name__ == "__main__":
    main()
