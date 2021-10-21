# code to demonstrate the use of a while loop #

#setting the variable of removed cables to 0
removed_cables = 0

#taking user input into variable cable
print("How many cables should i remove? ")
removed_cables = int(input())

#while removed cable variable is greater that 1, will display message and decrease the count by 1
while removed_cables >= 1:
    print("Removed cable")
    removed_cables = removed_cables - 1

