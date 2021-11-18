# code to demonstrate how to reverse a string using a for loop. #
def run():
    print("What phrase do you see? ")
    phrase = input()

    print("\nReversing...\n")
    print("The phrase is: ", end="")

    for position in range(len(phrase) - 1, -1, -1):
        print(phrase[position], end="")


if __name__ == "__main__":
    run()
