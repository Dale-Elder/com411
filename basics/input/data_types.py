# Code to demonstrate different uses of data types #
def run():
    name = input("What is your human name?:")
    age = int(input("How old are you (in years)?:"))
    height = float(input("How tall are you (in meters)?:"))
    weight = float(input("How much do you weight? (in kilograms)?:"))
    bmi = weight / (height * height)

    print(f"{name}you are {age} years old and your bmi is {bmi}")


if __name__ == "__main__":
    run()
