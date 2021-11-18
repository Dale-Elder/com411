# code to demonstrate the use of a user-defined function. #
def run():
    def listen():
        print("What sound did I hear? ")
        sound = input()
        print(f"\nThat was a loud {sound}!")

    listen()


if __name__ == "__main__":
    run()
