# code to demonstrate how to read a CSV file. #
# importing csv to get access to the csv reader
import csv


def read(file_path):
    with open(file_path) as file:
        csv_reader = csv.reader(file)
        headings = next(csv_reader)
        print(f"Headings:\n{headings}")
        print(f"Values:")
        for values in csv_reader:
            print(values)


def run():
    read("bots.csv")


if __name__ == "__main__":
    run()

