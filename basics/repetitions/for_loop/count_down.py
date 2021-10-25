# code to demonstrate counting down with a for loop. #

print("How far are we from the cave? ")
step = int(input())

for count in range(step):
    print(f"{step} steps remaining...\n")
    step -= 1

print("We have reached the cave! ")
