"""
Data Analysis Techdegree
Project 2 - Basketball Stats Project
"""
# Submitting for "Exceeds expectations"
# Please reject submission otherwise.
"""
By: Jabr Abumaali
Started: Nov 21, 2023
Completed: Dec 1, 2023
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
    exp_players = []
    nonexp_players = []
    num_experienced = 0
    
    for player in players:
        if player['experience']:
            num_experienced += 1
            exp_players.append(player)
        else:
            nonexp_players.append(player)
    
    num_experienced_team = int (num_experienced / len(teams))
    num_nonexp_team = int(len(nonexp_players) / len(teams))
    num_players_team = num_experienced_team + num_nonexp_team
    
    for team in teams:
        fixed = {}
        temp_players = []
        fixed["name"] = team
        count = 0
        while True:
            # Pop so each player is only used once.
            temp_players.append(exp_players.pop())
            count = count + 1
            if count >= num_experienced_team:
                count = 0
                break
        while True:
            temp_players.append(nonexp_players.pop())
            count = count + 1
            if count >= num_nonexp_team:
                count = 0
                break
        # Store the players for each team,
        # and the number of experienced/inexperienced.
        fixed["players"] = sorted(temp_players, key=lambda x: x['height'])
        fixed["num_exp"] = num_experienced_team
        fixed["num_nonexp"] = num_nonexp_team
        new_teams.append(fixed) 

    # Calculate and store average height.
    for team in new_teams:
        avg_height = 0
        count = 0
        for player in team['players']:
            avg_height += player['height']
            count += 1
        avg_height = avg_height/count
        team["avg_height"] = round(avg_height, 2)
    
    return new_teams

def show_stats(x, new_teams):
    print("\n")
    if x == "A":
        team = new_teams[0]
    elif x == "B":
        team = new_teams[1]
    elif x == "C":
        team = new_teams[2]
    print(f'Team: {team["name"]}')
    print("---------------------")
    print(f'Total Players: {len(team["players"])}')
    print(f'Total experienced: {team["num_exp"]}')
    print(f'Total inexperienced: {team["num_nonexp"]}')
    print(f'Average height: {team["avg_height"]}')
    
    player_list = []
    guardian_list = []
    for player in team["players"]:
        player_list.append(player["name"])
        for guardian in player["guardians"]:
            guardian_list.append(guardian)
    print(f'\nPlayers on team:\n{", ".join(player_list)}')
    print(f'\nGuardians on team:\n{", ".join(guardian_list)}')
    return 0


def menu():
    new_teams = balance_teams(TEAMS, clean_data_basic(PLAYERS))
    
    print("Basketball Team Stats Tool")
    while True:
        print("\n------- Menu -------\n\n")
        print("A) Display Team Stats\nB) Quit\n\n")

        x = input("Enter an option: ")

        if x == "A":
            print("Which team's stats would you like to view?\n")
            print("A) Panthers\nB) Bandits\nC) Warriors\n")
            x = input("Enter an option: ")
            if x == "A" or x == "B" or x == "C":
                show_stats(x, new_teams)
            else:
                print("Please select A, B, or C.")
        elif x == "B":
            break
        else:
            print("Please select a valid menu option")

    print("\n\nThank you for using Basketball Team Stats Tool.\nHave a nice day!")
    return 0

if __name__ == "__main__":
    menu()
