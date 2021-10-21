# code to demonstrate the use of a logical operator #

#asking for user a question
print("What did i hear? ")

#taking the user input into variable
hear = input()

#asking the user another question
print("What did i see? ")

# storing the user into into another variable
see = input()

# if condition with and operator to compair user input to expected results
if (hear == "grrr") and (see == "two red eyes"):
    print("There is a scary creature. \nI should get out of here!")
else: #else this will happen
    print("I am a little scared but i will continue.")

