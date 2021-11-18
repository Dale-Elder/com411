# code to demonstrate how to reverse a string using a for loop. #
def run():
    print("What phrase do you see? ")
    phrase = input()

    print("\nReversing...\n")
    print("The phrase is: ", end="")
    backwards = ""

    for letters in phrase:
        backwards = letters + backwards

    print(backwards)


if __name__ == "__main__":
    run()
