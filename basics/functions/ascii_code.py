<<<<<<< HEAD
# code to demonstrate the use of built-in functions: len, ord. #

print("Program Started!")
print("Please enter a standard character: ")
char = input()

for letter in char:
    value = ord(char)
    if len(char) == 1:
        print(f"The ASCII code for {char} is {value}.")
    else:
        print("Unexpected input.")


=======
# code to demonstrate the use of built-in functions len, ord #

print("Program started!\n")
character = input("Please enter a standard character: ")
if len(character) == 1:
    letter = character
    value = ord(character)
    print(f"The ASCII code for {letter} is {value}")
else:
    print("Oops!, that was not a valid, single character please try again.")
>>>>>>> 875e8831beffef9a49ec744fbae70b5a9c6c7c00
print("Program Ended!")
