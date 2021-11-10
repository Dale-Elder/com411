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


print("Program Ended!")
