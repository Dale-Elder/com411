# code to demonstrate a simple list #

def directions():
    directions = []
    # directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"] would work
    # but have chosen to use .append here, you could also remove an item from the list with .remove
    directions.append("Move Forward")
    directions.append("Move Backward")
    directions.append("Turn Left")
    directions.append("Turn Right")
    return directions


def run():
    print(directions())


if __name__ == "__main__":
    run()

