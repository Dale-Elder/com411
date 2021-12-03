# Code to demonstrate how to create a set from a list. #

def observed():
    observations = []
    for count in range(7):
        print("Please enter an observation:")
        observations.append(input())
    return observations


def run():
    print("Counting observations...")
    observations = observed()
    value = set()
    for observation in observations:
        data = (observation, observations.count(observation))
        value.add(data)
    for data in value:
        print(f"{data[0]} observed {data[1]} times.")


if __name__ == "__main__":
    run()
