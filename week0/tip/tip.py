def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # Remove the "$" and convert to float
    d = d.replace("$", "")
    return float(d)


def percent_to_float(p):
    # Remove the "%" and convert to float (divide by 100)
    p = p.replace("%", "")
    return float(p) / 100


main()
