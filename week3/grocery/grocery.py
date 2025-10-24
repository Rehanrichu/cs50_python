def main():
    groceries = {}

    while True:
        try:
            item = input().strip().lower()  # case-insensitive
            if item:  # ignore empty lines
                groceries[item] = groceries.get(item, 0) + 1
        except EOFError:
            print()  # move cursor to new line
            break

    # Sort and print
    for item in sorted(groceries.keys()):
        print(f"{groceries[item]} {item.upper()}")


if __name__ == "__main__":
    main()
