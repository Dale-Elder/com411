# Code to demonstrate the use of multiple nested statements. #
def run():
    print("Where should i look? ")
    where = input()
    bed = "in the bedroom"
    bath = "in the bathroom"
    lab = "in the lab"
    if where == bed:
        print("Where in the bedroom should i look? ")
        if input() == "under the bed":
            print("Found some shoe's but no battery.")
        else:
            print("Found some mess but no battery.")
    if where == bath:
        print("Where in the bathroom should i look? ")
        if input() == "in the bath":
            print("Found a rubber duck but no battery.")
        else:
            print("Found a wet surface but no battery.")
    if where == lab:
        print("Where in the lab should i look? ")
        if input() == "on the table":
            print("Yes! I found my battery!")
        else:
            print("Found some tools but no battery.")
    else:
        print("I do not know where that is but I will keep looking.")


if __name__ == "__main__":
    run()
