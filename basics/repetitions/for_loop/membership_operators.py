# code to demonstrate how to reverse a string using a for loop. #

print("What phrase do you see? ")
phrase = input()

print("\nReversing...\n")
print("The phrase is: ", end="")
backwards = ""


for letters in phrase:
    backwards = letters + backwards

print(backwards)
