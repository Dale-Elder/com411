# code to demonstrate the use of a nested decision statement. #

cover1 = input("Please the the cover type of the book hard / soft: ")
if cover1 == "soft":
    bound = input("is the book perfect bound? ")
    if cover1 == "soft" and bound == "yes":
        print("Soft cover, perfect bound books are very popular! ")
    else:
        print("soft covers with coils or stitches are great for short books")
else:
    print("Books with hard covers can be more expensive! ")
