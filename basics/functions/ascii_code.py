# code to demonstrate the use of built-in functions len, ord #

print("Program started!\n")
character = input("Please enter a standard character: ")
if len(character) == 1:
    letter = character
    value = ord(character)
    print(f"The ASCII code for {letter} is {value}")
else:
    print("Oops!, that was not a valid, single character please try again.")

