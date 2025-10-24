import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    # \b = word boundary so it only matches "um" as a word
    # re.IGNORECASE makes it case-insensitive
    ums = re.findall(r"\bum\b", s, re.IGNORECASE)
    return len(ums)


if __name__ == "__main__":
    main()
