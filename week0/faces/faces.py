# Function to convert emoticons to emojis
def convert(text):
    # Replace :) with 🙂 and :( with 🙁
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    return text

# Main function
def main():
    # Prompt user for input
    user_input = input()
    # Call convert function and print result
    print(convert(user_input))

# Call main when the file runs
if __name__ == "__main__":
    main()
