# code to demonstrate if...elif...else statement #
def run():
    up = "up"
    down = "down"
    left = "left"
    right = "right"
    choice = input("Towards which direction should i paint? ")
    if choice == up:
        print("I am painting in the upwards direction!")
    elif choice == down:
        print("I am painting in the downwards direction!")
    elif choice == left:
        print("I am painting in the leftwards direction!")
    else:
        print("I am painting in the rightwards direction!")


if __name__ == "__main__":
    run()
