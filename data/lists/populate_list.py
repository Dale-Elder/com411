# code to demonstrate how to populate a list. #

def directions():
    directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return directions


def menu():
    print("Please select a direction:")
    direction = directions()
    for index in range(len(direction)):
        print(f"{index}: {direction[index]}")
    index = int(input())
    return direction[index]


def run():
    route = []
    print("Working out escape route...")
    i = 5
    while i > 0:
        route.append(menu())
        i -= 1
    print(f"Escape route: {route}")


if __name__ == "__main__":
    run()
