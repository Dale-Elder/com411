# Code to demonstrate how to display a path using a line plot. #
import matplotlib.pyplot as plt


def coordinate():
    print("Please enter the x value:")
    x = input()
    print("Please enter the y value:")
    y = input()
    return x, y


def path():
    print("Retrieving path...")
    x_values = []
    y_values = []
    for count in range(4):
        data = coordinate()
        x_values.append(data[0])
        y_values.append(data[1])
    return [x_values, y_values]


def run():
    values = path()
    plt.plot(values[0], values[1], 'r--o')
    plt.xlabel("x values")
    plt.ylabel("y values")
    plt.show()


if __name__ == "__main__":
    run()
