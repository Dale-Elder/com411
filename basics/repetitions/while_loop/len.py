# code to demonstrate the use of a while loop with len function. #
def run():
    print("Please enter a phrase: ")
    phrase = str(input())
    number = 0
    bop = "Bop"
    while len(phrase) > number:
        print(f"{bop} ", end="")
        number += 1


if __name__ == "__main__":
    run()
