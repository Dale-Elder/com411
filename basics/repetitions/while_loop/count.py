# code to demonstrate the use of a while loop with a counter #

print("How many live cables must i avoid? ")
cables = int(input())

live_Cables = 0

n = 0

while cables > int(live_Cables):
    print("Avoiding....", end="")
    live_Cables += 1
    n +=1
    print(f"...Done! {n} live cable avoided.")

print("All live cables avoided. ")

