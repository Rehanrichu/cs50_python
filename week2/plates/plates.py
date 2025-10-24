def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Rule 1: Length between 2 and 6
    if len(s) < 2 or len(s) > 6:
        return False

    # Rule 2: First two characters must be letters
    if not s[0].isalpha() or not s[1].isalpha():
        return False

    # Rule 3: All characters must be letters or digits
    if not s.isalnum():
        return False

    # Rule 4: Numbers (if any) must be at the end
    for i in range(len(s)):
        if s[i].isdigit():
            # First number cannot be '0'
            if s[i] == "0":
                return False
            # After the first number, all remaining must be digits
            if not s[i:].isdigit():
                return False
            break

    # Passed all checks
    return True


main()
