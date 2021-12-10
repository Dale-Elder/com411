# Code to process the olympics data set. #
import tui

COL_YEAR = 9
COL_MEDAL = 14
COL_TEAM = 6


def list_years(data):
    tui.started("Listing years")
    years = set()
    for record in data:
        year = record[COL_YEAR]
        years.add(year)
    tui.display_years(years)
    tui.completed()


def tally_medals(data):
    tui.started("Tallying medals")
    medals = {"Gold": 0, "Silver": 0, "Bronze": 0}
    for record in data:
        medal = record[COL_MEDAL]
        if medal == "Gold":
            medals["Gold"] += 1
        elif medal == "Silver":
            medals["Silver"] += 1
        elif medal == "Bronze":
            medals["Bronze"] += 1
    tui.display_medal_tally(medals)
    tui.completed()


def tally_team_medals(data):
    tui.started("Tallying team medals")
    team_tally = {}
    for record in data:
        team = record[COL_TEAM]
        medal = record[COL_MEDAL]
        if medal not in ("Gold", "Silver", "Bronze"):
            continue
        if team in team_tally:
            team_tally[team][medal] += 1
        else:
            team_tally[team] = {"Gold": 0, "Silver": 0, "Bronze": 0}
            team_tally[team][medal] += 1
    tui.display_team_medal_tally(team_tally)
    tui.completed()
