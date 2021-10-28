# code to demonstrate the use of for loops in string indexing. #

print("What strange marking do you see? ")
marking = input()
index = 0

print("\nIdentifying...\n")

for position in range(0, len(marking), 1):
    print(f"index " + str(index) + ":", (marking[position]))
    index += 1

print("\nDone")
