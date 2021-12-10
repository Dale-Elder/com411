# Code for a Text User Interface, that can manipulate "The Olympics Data Set". #


def started(msg=""):
    print("-" * 85)
    print(f"Operation started: {msg}...\n")


def completed():
    print("\nOperation completed.")
    print("-" * 85)
    print()


def error(msg):
    print(f"Error! {msg}\n")


def menu():
    years = "List unique years"
    tally = "Tally up medals"
    team = "Tally up medals for each team"
    exit_program = "Exit the program"
    print(f"""Please select one of the following options:
    [years]{years:>20}
    [tally]{tally:>18}
    [team]{team:>33}
    [exit]{exit_program:>20}""")
    print("\nYour selection: ")
    selection = input()
    return selection


def display_medal_tally(tally):
    print(f"| {'Gold':<10} | {tally['Gold']:<10} |")
    print(f"| {'Silver':<10} | {tally['Silver']:<10} |")
    print(f"| {'Bronze':<10} | {tally['Bronze']:<10} |")


def display_team_medal_tally(team_tally):
    for team, tally in team_tally.items():
        print(team)
        print(f"\t Gold:{tally['Gold']}, Silver:{tally['Silver']}, Bronze:{tally['Bronze']}")


def display_years(years):
    sorted_years = sorted(years, reverse=True)
    for year in sorted_years:
        print(year)
