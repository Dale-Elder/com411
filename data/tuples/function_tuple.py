# code to demonstrate how to return a tuple from a function. #

def likelihood():
    likelihoods = (50, 38, 27, 99, 4)
    return min(likelihoods), max(likelihoods)


def run():
    min_max = likelihood()
    print(f"Minimum likelihood of falling: {min_max[0]}%")
    print(f"Maximum likelihood of falling: {min_max[1]}%")


if __name__ == "__main__":
    run()


