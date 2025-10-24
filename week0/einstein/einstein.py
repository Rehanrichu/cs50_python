def main():
    # Prompt user for mass as integer
    m = int(input("Mass (kg): "))

    # Speed of light (m/s)
    c = 300000000

    # Calculate energy
    E = m * (c ** 2)

    # Print result as integer
    print(E)


# Run main function
if __name__ == "__main__":
    main()
