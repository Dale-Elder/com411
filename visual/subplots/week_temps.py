# code to demonstrate how to display contents of a CSV file in subplots. #
import matplotlib.pyplot as plt
import csv


def read_data():
    with open("temps.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',', quotechar='"')
        header = next(csv_reader)
        week_temps = {'week1': [], 'week2': []}
        for row in csv_reader:
            week_temps['week1'].append(row[0])
            week_temps['week2'].append(row[1])
    return week_temps


def run():
    data = read_data()
    fig, axs = plt.subplots(2, 1, sharey='col')
    days = range(1, 8)
    axs[0].plot(days, data['week1'])
    axs[1].bar(days, data['week2'])
    axs[0].set_xlabel("Week 1")
    axs[0].set_ylabel("Temperature")
    axs[1].set_xlabel("Week 2")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    run()
