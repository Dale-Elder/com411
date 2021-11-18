# code to demonstrate the use of a nested decision statement. #
def run():
    cover1 = input("Please enter the cover type of the book (hard / soft): ")
    if cover1 == "soft":
        bound = input("is the book perfect bound? ")
        if cover1 == "soft" and bound == "yes":
            print("Soft cover, perfect bound books are very popular! ")
        else:
            print("soft covers with coils or stitches are great for short books")
    elif cover1 == "hard":
        print("Books with hard covers can be more expensive! ")
    else:
        print("I don't know what that book feels like")


if __name__ == "__main__":
    run()
