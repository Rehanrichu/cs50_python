# interpreter.py

def main():
    # Prompt user for expression
    expression = input("Expression: ")

    # Split input into x, y, z
    x, op, z = expression.split()

    # Convert x and z to integers
    x = int(x)
    z = int(z)

    # Perform calculation based on operator
    if op == "+":
        result = x + z
    elif op == "-":
        result = x - z
    elif op == "*":
        result = x * z
    elif op == "/":
        result = x / z

    # Print result formatted to one decimal place
    print(f"{result:.1f}")


if __name__ == "__main__":
    main()
