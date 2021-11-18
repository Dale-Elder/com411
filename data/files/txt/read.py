# code to demonstrate how to read a text file. #

def display_chars(file_path, number_of_chars):
    with open(file_path) as file:
        data = file.read(number_of_chars)
        print(f"The first {number_of_chars} characters are: ")
        print(data)


def display_line(file_path):
    with open(file_path) as file:
        line = file.readline().strip()
        print("The first line is: ")
        print(line)


def display_text(file_path):
    with open(file_path) as file:
        data = file.read()
        print("The full text is: ")
        print(data)


def run():
    display_chars("library.txt", 5)
    display_line("library.txt")
    display_text("library.txt")


if __name__ == "__main__":
    run()

