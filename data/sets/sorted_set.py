# Code to demonstrate how to manipulate and sort a set. #

def observed():
    observations = []
    for count in range(5):
        print("Please enter an observation:")
        observations.append(input())
    return observations


def remove_observations(observations):
    looping = True
    while looping:
        print("Do you wish to remove an observation? (yes/no)")
        choice = input()
        if choice.lower() == "yes":
            print("What observation do you wish to remove?")
            remove = input()
            observations.remove(remove)
            print(f"Done!\nRemoved {remove}\n")
        else:
            looping = False


def run():
    print("Counting observations...")
    observations = observed()
    remove_observations(observations)
    sorted_set = set()
    for observation in observations:
        data = (observation, observations.count(observation))
        sorted_set.add(data)
    print("\nObservations:")
    for data in sorted(sorted_set):
        print(f"{data[0]} observed {data[1]} times.")


if __name__ == "__main__":
    run()
