# code to demonstrate how a variable can be used as a counter. #
def run():
    even = 0
    odd = 0
    num1 = (int(input("Please enter the first whole number: ")))
    num2 = (int(input("Please enter the second whole number: ")))
    num3 = (int(input("Please enter the third whole number: ")))
    if num1 % 2 == 0:
        even += 1
    elif num1 % 2 != 0:
        odd += 1
    if num2 % 2 == 0:
        even += 1
    elif num2 % 2 != 0:
        odd += 1
    if num3 % 2 == 0:
        even += 1
    elif num3 % 2 != 0:
        odd += 1
    print(f"There are {even} even and {odd} odd numbers ")


if __name__ == "__main__":
    run()
