import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    pattern = r"^([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+)$"
    match = re.search(pattern, ip)
    if not match:
        return False

    for num in match.groups():
        # must be between 0–255 and no leading zeros (except single '0')
        if not 0 <= int(num) <= 255:
            return False
        if len(num) > 1 and num[0] == "0":
            return False
    return True


if __name__ == "__main__":
    main()
