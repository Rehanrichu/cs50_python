x = str(input("Give me a word: "))
list = ["A","E","I","O","U","a","e","i","o","u"]
for char in x :
    if char not in list :
        print(char, end="")
print()

