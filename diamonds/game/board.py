from random import randint

board = []


def board_creation():
    while len(board) < 8:
        row = []
        while len(row) < 8:
            cell = randint(1, 5)
            row.append(cell)
        board.append(row)
    return board


def show_board():
    for row in range(len(board)):
        for column in range(len(board[row])):
            print(board[row][column], end=" ")
        print()
    print()


def update_cell(cell_to_update, new_number):
    cell_to_update = new_number
    return