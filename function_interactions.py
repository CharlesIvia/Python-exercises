#Simple guessing game

from random import shuffle

my_list = ["", "O", ""]


def shuffle_list(my_list):
    shuffle(my_list)
    return my_list


def player_guess():
    guess = ""

    while guess not in ["0", "1", "2"]:
        guess = input("Pick a number: 0, 1 or 2:  ")
    return int(guess)


def check_guess(my_list, guess):
    if my_list[guess] == "O":
        print("Correct")
    else:
        print("Wrong! Better luck next time.")
        print(my_list)


#Set up fn

my_list = my_list;

mixed_list = shuffle_list(my_list)

guess = player_guess()

check_guess(mixed_list, guess)
