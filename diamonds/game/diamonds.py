import os
from random import randint
from diamonds.game.neighbors import Neighbors
from diamonds.game.board import board_creation, show_board

players_numbers = {1: str(randint(1, 5)), 2: str(randint(1, 5))}
points = {1: 0, 2: 0}
victories = {}
board = board_creation()


def menu():
    clear_terminal()
    print(" *************")
    print("***************", end="              Main Menu")
    print(end="\n   ")
    print("DIAMONDS", end="         To continue select an option")
    print(end="\n ")
    print("*************", end="")
    print(end="\n  ")
    print("***********", end="                  1. Play")
    print(end="\n   ")
    print("*********", end="                   2. Highscores")
    print(end="\n    ")
    print("*******", end="                    3. Exit")
    print(end="\n     ")
    print("*****", end="")
    print(end="\n      ")
    print("***", end="")
    print(end="\n       ")
    print("*", end="")
    print(end="\n  ")
    selected_option = input("                             ")
    return main_menu_verify_option(selected_option)


def main_menu_verify_option(selected_option):
    clear_terminal()
    available_options = [["1", "1.", "Play", "1. Play"],
                         ["2", "2.", "Highscores", "2. Highscores"],
                         ["3", "3.", "Exit", "3. Exit"]]
    if selected_option in available_options[0]:
        return game_menu()
    elif selected_option in available_options[1]:
        pass
    elif selected_option in available_options[2]:
        return input("¡Come back soon!")
    else:
        print("Error: This isn't a valid option.\n")
        input("Press a key to continue...")
        return menu()


def game_menu():
    clear_terminal()
    print("         Game Menu")
    print("To continue select an option\n")
    print("         1. Player vs Player")
    print("         2. Player vs Computer")
    print("         3. Go back\n")
    selected_option = input()
    return game_menu_option_verifier(selected_option)


def game_menu_option_verifier(selected_option):
    clear_terminal()
    available_options = [["1", "1.", "Player vs Player", "1. Player vs Player"],
                         ["2", "2.", "Player vs Computer",
                          "2. Player vs Computer"],
                         ["3", "3.", "Go back", "3. Go back"]]
    if selected_option in available_options[0]:
        return start_game()
    elif selected_option in available_options[1]:
        pass
    elif selected_option in available_options[2]:
        return menu()
    else:
        print("Error: This isn't a valid option.\n")
        input("Press a key to continue...")
        return game_menu()


def start_game():
    clear_terminal()
    show_board()
    players_positions = {1: [], 2: []}
    for player in range(1, 3):
        print("Number for player " + str(player) +
              " is " + str(players_numbers[player]) + "\n")
        players_positions[player].append(int(input(
            "Insert the row number where you want to move ")) - 1)
        players_positions[player].append(int(input(
            "Insert the column number where you want to move ")) - 1)
        row = players_positions[player][0]
        column = players_positions[player][1]
        if - 1 in players_positions[player]:
            player = (1 - player) + 2
            return claim_victory(player)
        board[row][column] = players_numbers[player]
        near_numbers = get_number_position(board,
                                           players_positions[player],
                                           players_numbers[player], player)
        calculate_score(players_positions[player], players_numbers[player],
                        player, near_numbers)
        board[row][column] = players_numbers[player]
        print("Player " + str(player) + " score: " +
              str(points[player]) + "\n")
        input("Press a key to continue...\n")
        show_board()
        players_numbers[player] = str(
            board[players_positions[player][0]]
            [players_positions[player][1]])
    return start_game()


def claim_victory(player):
    print("¡Congratulations, player " + str(player) + " has won!\n")
    input("Press a key to play again...")
    return menu()


def calculate_score(player_position, player_number, player, near_numbers):
    for neighbor in near_numbers:
        if (int(player_number) == board[neighbor[0]][neighbor[1]]):
            points[player] += 1
            board[neighbor[0]][neighbor[1]] = randint(1, 5)
            near_numbers = get_number_position(board,
                                               [neighbor[0],
                                                neighbor[1]],
                                               player_number, player)
            calculate_score(player_position, player_number,
                            player, near_numbers)
    return


def clear_terminal():
    return os.system('cls' if os.name == 'nt' else 'clear')


board = board_creation()
menu()
