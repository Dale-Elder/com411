# code to review the use of a decisions, nesting and logical operators. #
# taking users name and age into variables
print("What is your name? ")
name = input()
print("How old are you? ")
age = input()
#displaying those variables back to the user with a simple message
#then asking user another question, storing that into another variable
print(f"Hello {name}, you are {age} years old\nHow are you today? ")
feeling = input()
#multiple conditions, and operators based off user input
if (feeling == "good") or (feeling == "great"):
    print(f"Glad your feeling {feeling}, me too!")
elif (feeling == "crap") or (feeling == "miserable"):
    print(f"Oh im sorry your feeling {feeling}")
else:
    pass
#asking the user a final question and storing response into variable
print("How is the weather today?")
weather = input()
#another conditional check with multiple decisions and operators
if (weather == "good") or (weather == "sunny") or (weather == "hot"):
    print(f"{weather}Sounds nice {name}, hope you enjoy your day! \n:)")
elif (weather == "cold") or (weather == "wet") or (weather == "raining"):
    print(f"Oh no {name} {weather} is not ideal, make sure you wrap up warm!")
else:
    print("Hmmm im not really sure what to say.")
