camelCase = str(input("camelCase: "))

for letter in camelCase:

    if letter.isupper():
        print(f"_" + letter.lower(), end="")
    else:
        print(letter, end="")


