# code to demonstrate the use of multiple function calls. #
def run():
    def display_in_box(message):
        art = 6 + len(message)
        print("*" * art)
        print(f"|| {message} ||")
        print("*" * art)

    def display_lower(message):
        print(message.lower())

    def display_upper(message):
        print(message.upper())

    def display_mirror(message):
        mirrored = ""
        for letter in reversed(message):
            mirrored += letter
        print(f"{message} // {mirrored}")

    def repeated(message):
        print("How many time's should i repeat the message?")
        repeat = int(input())

        for rep in range(repeat):
            if rep % 2 == 0:
                print(message.upper(), end=" ")
            else:
                print(message.lower(), end=" ")

    def run_program():
        print("Please enter a word:")
        message = input()
        print("(1) Display in a box")
        print("(2) Display Lower-case")
        print("(3) Display Upper-case")
        print("(4) Display Mirrored")
        print("(5) Display Repeated")
        print("How would you like me to manipulate the word?")
        manipulate = str(input())
        if manipulate == "1":
            display_in_box(message)
        elif manipulate == "2":
            display_lower(message)
        elif manipulate == "3":
            display_upper(message)
        elif manipulate == "4":
            display_mirror(message)
        elif manipulate == "5":
            repeated(message)
        else:
            print("Unknown choice...")

    run_program()
    print("\nProgram finished!")


if __name__ == "__main__":
    run()
