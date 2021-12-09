# Code to demonstrate how to create a dictionary of dictionaries. #

def short_pattern():
    pattern = {"sequence": "101", "occurrences": 5}
    return pattern


def medium_pattern():
    pattern = {"sequence": "111000", "occurrences": 25}
    return pattern


def long_pattern():
    pattern = {"sequence": "1100110011001100", "occurrences": 50}
    return pattern


def run():
    print("Analysing patterns...")
    sequences = {"Short Sequence": short_pattern(),
                 "Medium Sequence": medium_pattern(),
                 "Long Sequence": long_pattern()}
    for key, value in sequences.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    run()
