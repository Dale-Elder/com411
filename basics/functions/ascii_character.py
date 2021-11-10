# code to demonstrate the use of built-in functions: abs, range, chr. #

print("Program started!\n")
code = int(input("Please enter an ASCII code: "))
if code in range(32, 126, 1):
    character = chr(code)
    value = code
    print(f"\nThe character represented by the ASCII code {value} is {character}")
else:
    print("Oops!, that was not a valid ASCII code, please try again.")
print("\nProgram Ended!")
