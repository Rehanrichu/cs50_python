d

def main():
    # Prompt for input and normalize (strip spaces + lowercase)
    greeting = input("Greeting: ").strip().lower()

    # Check conditions
    if greeting.startswith("hello"):
        print("$0")
    elif greeting.startswith("h"):
        print("$20")
    else:
        print("$100")

if __name__ == "__main__":
    main()
