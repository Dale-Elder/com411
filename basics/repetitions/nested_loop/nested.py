# code to demonstrate the use of one loop nested in another #

rows = int(input("How many rows should i have? "))
columns = int(input("How many columns should i have? "))
art = ":-)"
print("Here i go: \n")

for row in range(0, rows, 1):
    for column in range(0, columns, 1):
        print(art, end="")
    print()
