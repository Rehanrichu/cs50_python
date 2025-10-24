# Prompt the user for camelCase input
camel = input("camelCase: ")

# Prepare an empty string for snake_case
snake = ""

# Loop through each character
for char in camel:
    if char.isupper():
        # Add underscore before uppercase letters (except at the start)
        snake += "_" + char.lower()
    else:
        snake += char

# Output result
print("snake_case:", snake)
