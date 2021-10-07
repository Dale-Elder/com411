# code to demonstrate the use of string operators #
count1 = int(input("Please enter the number of lives:"))
count2 = int(input("Please enter the energy level:"))
count3 = int(input("Please enter the shield level:"))
lives = "♥"
energy = "♦"
shield = "🔰"
print("")
print("Health has been set.")
print("")
print(f"Lives: {count1 * lives} ")
print(f"Energy: {count2 * energy}")
print(f"Shield: {count3 * shield}")
