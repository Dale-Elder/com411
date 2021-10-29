# code to demonstrate the use of a user-defined function with a nested decision. #

def identify():
    print("What lies before us? ")
    seen = input()
    if seen == "a large boulder":
        print("\nIt's time to run!")
    else:
        print("\nWe will be fine.")


identify()
