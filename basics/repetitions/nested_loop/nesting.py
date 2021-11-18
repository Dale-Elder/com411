# code to demonstrate the use of nested loops and decisions. #
def run():
    sequence = input("Please enter a sequence ")
    mark = input("Please enter the character for the marker ")
    marker_1 = -1
    marker_2 = -1
    for distance in range(0, len(sequence), 1):
        letter = sequence[distance]
        if letter == mark:
            if marker_1 == -1:
                marker_1 = distance
            else:
                marker_2 = distance
    print(f"The distance between the markers is {marker_2 - marker_1 -1}.")


if __name__ == "__main__":
    run()
