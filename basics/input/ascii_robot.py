# Display Ascii Art #
def run():
    eye = input("Please pick a Character for the eyes:")
    mouth = input("Please pick a Character for the mouth:")
    print("\t\\/\t")
    print("##########")
    print(f"# \t{eye*2}\t #")
    print(f"#\t{mouth*3}\t #")
    print("##########")


if __name__ == "__main__":
    run()
