# code to demonstrate counting down with a for loop. #
def run():
    print("How far are we from the cave? ")
    step = int(input())

    for count in range(step):
        print(f"{step} steps remaining...\n")
        step -= 1

    print("We have reached the cave! ")


if __name__ == "__main__":
    run()
