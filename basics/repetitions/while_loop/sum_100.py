# code to demonstrate the use of summing with a while loop. #
def run():
    print("Calculating the sum of the first 100 numbers...")
    num = 0
    sum = 0
    while num < 101:
        sum += num
        num += 1
    print(f"...Done! The answer is {sum}")


if __name__ == "__main__":
    run()
