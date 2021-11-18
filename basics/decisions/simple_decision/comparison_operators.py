# code to demonstrate the use of comparison operators #
def run():
    num1 = input("Please enter the first number. ")
    num2 = input("Please enter the second number. ")
    if num1 > num2:
        print("The first number is the smallest ")
    elif num1 < num2:
        print("The second number is the smallest ")
    elif num1 == num2:
        print("Both numbers are equal! ")


if __name__ == "__main__":
    run()
