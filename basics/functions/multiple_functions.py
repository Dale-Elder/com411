# code to demonstrate the implementation of multiple user-defined functions. #
def run():
    def display_ladder(steps):
        for step in range(0, steps, 1):
            print(" |  |")
            print(" ====")
        print(" |  |")

    def create_ladder():
        print("How many steps remain?")
        remain = int(input())
        display_ladder(remain)

    create_ladder()


if __name__ == "__main__":
    run()
