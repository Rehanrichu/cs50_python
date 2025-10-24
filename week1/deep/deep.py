# deep.py

def main():
    # Prompt user with the actual question
    ans = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip().lower()

    # Normalize input: treat hyphens as spaces, collapse extra spaces
    ans = ans.replace("-", " ")
    ans = " ".join(ans.split())

    # Check valid answers
    if ans == "42" or ans == "forty two":
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()
