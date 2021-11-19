# code to demonstrate how to export data to a JSON file. #
import json


def read(file_path):
    print("Reading...", end="")
    with open(file_path) as file:
        data = json.load(file)
    print("Done!")
    return data


def save(file_path, data_saved):
    print("Exporting...", end="")
    with open(file_path, "w") as file:
        json.dump(data_saved, file, indent=4)
    print("Done!")


def run():
    json_data = read("robocity.json")
    save("exported_json", json_data)


if __name__ == "__main__":
    run()
