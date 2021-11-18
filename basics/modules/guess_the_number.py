# code to demonstrate the import and use of a module. #
def run():
    import random as rnd

    print("Please enter the minimum value: ")
    Min = int(input())
    print("Please enter the maximum value: ")
    Max = int(input())

    num1 = rnd.randrange(Min, Max, 1)
    guesses = 0

    print(f"I am thinking of a number between {Min} and {Max}. \nCan you guess what it is?")

    guess = int(input())
    guesses += 1
    while guess != num1:
        if guess < num1:
            print("Your guess was too low.\nTry again: ")
            guess = int(input())
            guesses += 1
        elif guess > num1:
            print("Your guess was too high.\nTry again: ")
            guess = int(input())
            guesses += 1
    else:
        print(f"Congratulations! You guessed my number in {guesses} guesses!")


if __name__ == "__main__":
    run()
