# code to demonstrate the use of a while loop with len function. #

print("Please enter a phrase: ")
phrase = str(input())
number = 0
bop = "Bop"
while len(phrase) > number:
    print(f"{bop} ", end="")
    number += 1
