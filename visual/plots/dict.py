# Code to demonstrate how to display line plots using a dictionary. #
import matplotlib.pyplot as plt
import random as rnd


def data():
    paths = {}

    print("What type of line would you like? (:, -- or -)")
    line = input()

    print("What colour would you like? (r, g or b)")
    colour = input()

    print("What type of marker would you like? (o, s or ^)")
    marker = input()

    paths['line'] = line
    paths['colour'] = colour
    paths['marker'] = marker

    return paths


def generate():
    print("How many lines would you like to display?")
    num_lines = int(input())

    for lines in range(num_lines):
        values = data()
        x = rnd.sample(range(1, 10), 5)
        y = rnd.sample(range(1, 10), 5)
        line_format = f"{values['colour']}{values['line']}{values['marker']}"
        plt.plot(x, y, line_format)

    plt.show()


def run():
    print("Running...")
    generate()
    print("Done!")


if __name__ == "__main__":
    run()
