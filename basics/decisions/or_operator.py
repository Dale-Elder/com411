# code to demonstrate the use of a logical or operator. #
def run():
    # taking user input
    print("What type of adventure should i have? ")
    choice = input()

    if (choice == "scary") or (choice == "short"):
        print("Entering the dark forest!. ")
    elif (choice == "safe") or (choice == "long"):
        print("Taking the safe route!. ")
    else:
        print("Not sure which route to take...")


if __name__ == "__main__":
    run()

