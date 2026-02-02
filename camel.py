camelCase = str(input("camelCase: "))

#converts camel case into snake case
for letter in camelCase:

    if letter.isupper():
        print(f"_" + letter.lower(), end="")
    else:
        print(letter, end="")


