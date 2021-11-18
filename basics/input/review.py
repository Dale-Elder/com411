# Creating a basic input/output program #
def run():
    print("Hello, My name is Beep!")
    name = str(input("What's your name? "))
    print(f"Well hello there {name} it's nice to meet you!")
    print("\n\n\n")
    print("#"*15)


if __name__ == "__main__":
    run()
