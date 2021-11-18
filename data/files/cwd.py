# code to display information about the current working directory #
# importing os module
import os


# creating a function that displays the current working directory and lists the files contained within
def cwd():
    path = os.getcwd()
    print(f"The Current Working Directory is: {path}")
    print(f"The directory contains the following files: ")
    for file in os.listdir(path):
        print(file)


# creating a run function that calls the other function and displays some text
def run():
    print("Processing...")
    cwd()


if __name__ == "__main__":
    run()
