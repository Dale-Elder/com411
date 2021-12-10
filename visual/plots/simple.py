# Code to demonstrate how to display a simple line plot. #
import matplotlib.pyplot as plt


def display(x_value, y_value):
    plt.plot(x_value, y_value)
    plt.show()


def run():
    x_values = [1, 2, 3, 4, 5]
    y_values = [1, 4, 9, 16, 25]
    display(x_values, y_values)


if __name__ == "__main__":
    run()
