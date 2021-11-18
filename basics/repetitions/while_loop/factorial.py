# code to demonstrate the use of a while loop in calculating the factorial of a number #
def run():
    print("Please enter a number: ")
    num1 = int(input())

    count = 0
    total = 1

    while count < num1:
        count = count + 1
        total = total * count

    print(f"The factorial is {total}")


if __name__ == "__main__":
    run()
