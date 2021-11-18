# code to demonstrate the use of a simple for loop #
def run():
    print("What level of brightness is required?")
    light = int(input())

    print("\nAdjusting brightness...\n")

    for count in range(2, light + 1, 2):
        print(f"Beep's brightness level: {'*' * count}")
        print(f"Bop's brightness level: {'*' * count}\n")

    print("Adjustments complete!")


if __name__ == "__main__":
    run()
