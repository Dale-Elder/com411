# code to demonstrate the use of a user-defined function with multiple parameters. #
def run():
    def climb_ladder(steps_remaining, steps_crossed):
        if steps_remaining > steps_crossed:
            print("Still some way to go!")
        else:
            print("We are almost there!")

    climb_ladder(5, 2)
    climb_ladder(2, 5)


if __name__ == "__main__":
    run()
