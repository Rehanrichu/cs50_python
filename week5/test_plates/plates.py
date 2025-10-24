
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Rule 1: Length check (2–6)
    if len(s) < 2 or len(s) > 6:
        return False

    # Rule 2: Must start with two letters
    if not s[0:2].isalpha():
        return False

    # Rule 3 & 4: Numbers only at end, no leading zero
    number_started = False
    for char in s:
        if char.isdigit():
            if not number_started:
                # first digit found
                number_started = True
                if char == "0":
                    return False  # leading zero not allowed
        else:
            # if letter appears after number, invalid
            if number_started:
                return False

    # Rule 5: No punctuation or spaces
    if not s.isalnum():
        return False

    return True


if __name__ == "__main__":
    main()
