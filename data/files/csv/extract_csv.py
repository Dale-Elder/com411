# code to extract data from the CSV file using an index value #
import csv


def extract(file_path):
    print("Extracting...", end="")
    with open(file_path) as file:
        csv_reader = csv.reader(file)
        headings = next(csv_reader)
        names = ""
        for values in csv_reader:
            names += f"{values[1]}\n"
        print(f"Done! The extracted names are as follows:\n{names}")


def run():
    extract("bots.csv")


if __name__ == "__main__":
    run()

