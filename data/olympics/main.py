# the main module for the Olympics program. #
import csv
import process
import tui


def read_data(file_path):
    tui.started(f"Reading data from {file_path}")
    with open(file_path) as file:
        csv_reader = csv.reader(file)
        headings = next(csv_reader)
        data = []
        for value in csv_reader:
            data.append(value)
    tui.completed()
    return data


def run():
    athlete_data = read_data("athlete_events.csv")

    while True:
        selection = tui.menu()
        if selection == "years":
            tui.display_years()
        elif selection == "tally":
            tui.display_medal_tally()
        elif selection == "team":
            tui.display_team_medal_tally()
        elif selection == "exit":
            break
        else:
            tui.error("Invalid Selection!")


if __name__ == "__main__":
    run()
