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


def display_medal_tally(tally):
    for tally in tally.items():
        print(f"|{'Gold':<15}|{tally['Gold']:<15}")
        print(f"|{'Silver':<15}|{tally['Silver']:<15}")
        print(f"|{'Bronze':<15}|{tally['Bronze']:<15}")


def display_team_medal_tally(team_tally):
    for team, tally in team_tally.items():
        print(team)
        print(f"\t Gold:{tally['Gold']}, Silver:{tally['Silver']}, Bronze:{tally['Bronze']}")


def display_years(years):
    for year in years.sorted:
        print(year)
