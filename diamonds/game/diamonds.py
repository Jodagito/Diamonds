import os
from random import randint
from diamonds.game.neighbors import Neighbors
from diamonds.game.board import board_creation, show_board

players_numbers = {1: str(randint(1, 5)), 2: str(randint(1, 5))}
points = {1: 0, 2: 0}
victories = {}
board = board_creation()


def print_main_menu():
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
    return receive_main_menu_option()

def receive_main_menu_option():
    selected_option = input("                             ")
    return verify_main_menu_selection(selected_option)

def verify_main_menu_selection(selected_option):
    try:
        clear_terminal()
        available_options = [["1", "1.", "Play", "1. Play"],
                            ["2", "2.", "Highscores", "2. Highscores"],
                            ["3", "3.", "Exit", "3. Exit"]]
        if selected_option in available_options[0]:
            return print_game_menu()
        elif selected_option in available_options[1]:
            pass
        elif selected_option in available_options[2]:
            return input("¡Come back soon!")
        else:
            raise ValueError
    except ValueError:
        print("Error: This isn't a valid option.\n")
        input("Press a key to continue...")
        return print_main_menu()


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
            return print_main_menu()
    else:
        print("Error: This isn't a valid option.\n")
        input("Press a key to continue...")
        return game_menu()


def start_game():
    clear_terminal()
    show_board()
    players_positions = {1: [], 2: []}
    for player in range(1, 3):
        play_turn(player, players_positions)
        show_board()
        players_numbers[player] = board[players_positions[player]
                                        [0]][players_positions[player][1]]
    return start_game()


def play_turn(player, players_positions):
    print("Number for player " + str(player) +
          " is " + str(players_numbers[player]) + "\n")
    players_positions[player].append(int(input(
        "Insert the row number where you want to move ")) - 1)
    players_positions[player].append(int(input(
        "Insert the column number where you want to move ")) - 1)
    row = players_positions[player][0]
    column = players_positions[player][1]
    if -1 in players_positions[player]:
        player = (1 - player) + 2
        return claim_victory(player)
    board[row][column] = players_numbers[player]  # Is duplicated
    neighbors = Neighbors(
        board, player, players_numbers[player], players_positions[player])
    calculate_score(players_positions[player], players_numbers[player],
                    player, neighbors)
    # board[row][column] = players_numbers[player]  # Must be fixed
    print("Player " + str(player) + " score: " +
          str(points[player]) + "\n")
    input("Press a key to continue...\n")
    return


def claim_victory(player):
    print("¡Congratulations, player " + str(player) + " has won!\n")
    input("Press a key to play again...")
    return print_main_menu()


def calculate_score(player_position, player_number, player, neighbors):
    player_number_neighbors = get_player_number_neighbors(neighbors)
    for number_neighbor in player_number_neighbors:
        print(board[number_neighbor[0]][number_neighbor[1]])
        if int(player_number) == board[number_neighbor[0]][number_neighbor[1]]:
            print(number_neighbor)
            points[player] += 1
            board[number_neighbor[0]][number_neighbor[1]] = randint(1, 5)
            neighbors.update_attributes(
                board, player, player_number, player_position)
            calculate_score(player_position, player_number,
                            player, neighbors)
    return


def get_player_number_neighbors(neighbors):
    number_position = neighbors.get_number_position()
    number_orientation = neighbors.get_orientation()
    formula_to_use = neighbors.select_distance_formula(
        number_position, number_orientation)
    return neighbors.get_neighbors(formula_to_use)


def clear_terminal():
    return os.system('cls' if os.name == 'nt' else 'clear')
