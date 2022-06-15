#  Scissors, Paper, Rock, Lizard, Spock
import random

list_of_figure = ['Scissors', 'Paper', 'Rock', 'Lizard', 'Spock']
dict_of_victory = {'Paper': ['Spock', 'Rock'],
                   'Scissors': ['Lizard', 'Papers'],
                   'Rock': ['Lizard', 'Scissors'],
                   'Lizard': ['Spock', 'Paper'],
                   'Spock': ['Scissors', 'Rock']}


def game(user_choice):
    if computer_figure in dict_of_victory[user_choice]:
        result_game = 'Player WIN'
    elif computer_figure == user_choice:
        result_game = 'DRAW'
    else:
        result_game = 'Player DEFEAT'
    return result_game


def check_argument(user_choice):
    while user_choice not in dict_of_victory.keys():
        result = f'\nInvalid input {user_choice}\
              \nYour choice once of: rock, paper, scissors, lizard, spock?'
        return result
    else:
        result = 'Its okay'
    return result


computer_figure = list_of_figure[random.randint(0, len(list_of_figure) - 1)]
player_figure = input('Your figure? ')
result_check = check_argument(player_figure.capitalize())
print(result_check)
if result_check == 'Its okay':
    print(f'Player: {player_figure.capitalize()}\nComputer: {computer_figure}')
    print(game(player_figure.capitalize()))
else:
    pass

once_again = input('Repeat (Y/N)?')

while once_again != 'Y' or once_again != 'N':
    while once_again == 'Y':
        computer_figure = list_of_figure[random.randint(0, len(list_of_figure) - 1)]
        player_figure = input('Your figure? ')
        result_check = check_argument(player_figure.capitalize())
        if result_check == 'Its okay':
            print(f'Player: {player_figure.capitalize()}\nComputer: {computer_figure}')
            print(game(player_figure.capitalize()))
            once_again = input('Repeat (Y/N)?')
        else:
            print(f'\nInvalid input {player_figure}\
                          \nYour choice once of: rock, paper, scissors, lizard, spock?')
            once_again = input('Repeat (Y/N)?')
    if once_again == 'N':
        print('Thanks for playing')
        break
    else:
        print(f'Invalid input {once_again}')
        once_again = input('Repeat (Y/N)?')
