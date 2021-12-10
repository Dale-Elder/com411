# Code to demonstrate how to display simple subplots. #
import matplotlib.pyplot as plt


def read_data(file_path):
    with open(file_path) as file:
        temps = []
        for line in file:
            temps.append(float(line.strip()))
        return temps


def run():
    data = read_data("temps.txt")
    fig, axs = plt.subplots(1, 2, sharex='row')
    days = range(1, 8)
    axs[0].plot(days, data)
    axs[1].bar(days, data)
    axs[0].set_xlim(min(days), max(days))
    axs[1].set_xlim(min(days), max(days))
    axs[0].set_xlabel("Day")
    axs[0].set_ylabel("Temperature")
    axs[1].set_xlabel("Day")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    run()
