# Added code to demonstrate the use of a while loop in performing calculations with user input. #

print("How many numbers should i sum up? ")
num1 = int(input())
num2 = 0
sum1 = 0

while num2 < num1:
    print(f"Please enter number {num2+1} of {num1}:")
    num3 = int(input())
    sum1 = sum1 + num3
    sum1 = sum1 + 1
    num2 += 1

print(f"The answer is {sum1 - num2}")
