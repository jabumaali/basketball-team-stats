"""
Data Analysis Techdegree
Project 2 - Basketball Stats Project
"""
# Submitting for "Exceeds expectations"
# Please reject submission otherwise.
"""
By: Jabr Abumaali
Started: Nov 21, 2023
Completed: ------------
--------------------------------
"""
from constants import TEAMS, PLAYERS

def clean_data_basic(data):
    cleaned = []
    for user in data:
        fixed = {}
        fixed["name"] = user["name"]
        fixed["guardians"] = user["guardians"].split(" and ")
        if user["experience"] == "YES":
            fixed["experience"] = True
        else:
            fixed["experience"] = False
        fixed["height"] = int(user["height"].split()[0])
        cleaned.append(fixed)
    return cleaned

def balance_teams(teams, players):
    new_teams = []
    num_players_team = len(players) / len(teams)
    for team in teams:
        fixed = {}
        fixed["name"] = team
        print(len(players))
        fixed["players"] = players
        new_teams.append(fixed)
    return new_teams

def show_stats(team):
    print("Hi")
    for item in team:
        print(item)
    return team

new_players = clean_data_basic(PLAYERS)
new_teams = balance_teams(TEAMS, new_players)


print("Basketball Team Stats Tool")

while True:
    print("---- Menu ----\n\n")
    print("A) Display Team Stats\nB) Quit\n\n")

    x = input("Enter an option: ")

    if x == "A":
        show_stats(new_teams)
    elif x == "B":
        break
    else:
        print("Please select a valid menu option")

print("\n\nThank you for using Basketball Team Stats Tool.\nHave a nice day!")

    
