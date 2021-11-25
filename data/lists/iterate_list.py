# code to demonstrate how to iterate a list. #

def directions():
    direction = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return direction


def menu():
    print("Please select a direction:")
    direction = directions()
    for index in range(len(direction)):
        print(f"{index}: {direction[index]}.")


def run():
    menu()


if __name__ == "__main__":
    run()


