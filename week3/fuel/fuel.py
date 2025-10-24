def main():
    while True:
        try:
            fraction = input("Fraction: ")
            x, y = fraction.split("/")
            x = int(x)
            y = int(y)

            # Reject non-positive integers and invalid fractions
            if y == 0 or x > y or x < 0 or y < 0:
                raise ValueError

            percent = round((x / y) * 100)

            if percent <= 1:
                print("E")
            elif percent >= 99:
                print("F")
            else:
                print(f"{percent}%")
            break

        except (ValueError, ZeroDivisionError):
            continue


if __name__ == "__main__":
    main()
