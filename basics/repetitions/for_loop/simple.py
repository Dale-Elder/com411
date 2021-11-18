# code to demonstrate the use of a simple for loop #
def run():
    print("How many mountains should i display: ")
    mountain = int(input())

    print("\nDisplaying...\n")
    for count in range(mountain):
        print("       __")
        print("      /  \_")
        print("     / ^   \_")
        print("    /^  ^  ^ \_")
        print("  _/ ^   ^   ^ \_")
        print(" / ^  ^  ^^  ^   \_")
        print("\n")

    print("Done!")


if __name__ == "__main__":
    run()
