# code to demonstrate the use of a while loop with ascii art. #

charge = ("■")

print("How many bars should be charged? ")
charged = int(input())

bars_Charged = 0

while charged > bars_Charged:
    print("Charging:", end="")
    bars_Charged += 1
    print(f"{charge * bars_Charged}")


print("The battery is fully charged. ")



