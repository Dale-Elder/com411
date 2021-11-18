# code to demonstrate the use of a modulus operator. #
def run():
    num1 = (int(input("Please enter a whole number. ")))

    if num1 % 2 == 0:
        print(f"the number {num1} is an even number. ")
    elif num1 % 2 != 0:
        print(f"the number {num1} is an odd number. ")


if __name__ == "__main__":
    run()
