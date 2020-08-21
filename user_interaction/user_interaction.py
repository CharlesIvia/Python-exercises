#Disaplay game fn
def display_game(game_list):
    print("Here is the current list")
    print(game_list)

#Choose position


def position_choice():
    choice = "wrong"
    while choice not in ["0", "1", "2"]:
        choice = input("Pick a position (0,1,2)")
        if choice not in ["0", "1", "2"]:
            print("Sorry, invalid choice")
    return int(choice)

#Replacement choice


def replacement_choice(game_list, position):
    user_placement = input("Type a string to place at a position")
    game_list[position] = user_placement

    return game_list