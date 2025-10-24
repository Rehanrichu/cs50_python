def main():
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    while True:
        date = input("Date: ").strip()

        try:
            # Format: MM/DD/YYYY
            if "/" in date:
                month, day, year = date.split("/")
                month = int(month)
                day = int(day)
                year = int(year)

            # Format: Month DD, YYYY
            elif "," in date:
                month_name, day, year = date.replace(",", "").split()
                month = months.index(month_name.capitalize()) + 1
                day = int(day)
                year = int(year)

            else:
                raise ValueError

            # Validate ranges
            if not (1 <= month <= 12 and 1 <= day <= 31):
                raise ValueError

            print(f"{year:04}-{month:02}-{day:02}")
            break

        except (ValueError, IndexError):
            continue


if __name__ == "__main__":
    main()
