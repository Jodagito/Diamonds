board = []


def get_number_position(game_board, player_position, player_number, player):
    board = game_board
    position = ""
    player_row = player_position[0]
    player_column = player_position[1]
    if player_row in [0, len(board) - 1] and player_column in [0, len(board) - 1]:
        position = "corners"
        neighbors = get_orientation(
            player_number, player_position, position)
    elif (player_row not in [0, len(board) - 1] and
          player_column not in [0, len(board) - 1]):
        position = "middle"
        neighbors = get_neighbors(player_number, player_position, position)
    else:
        position = "bounds"
        neighbors = get_orientation(
            player_number, player_position, position)
    return neighbors


def get_orientation(player_number, player_position, position):
    player_row = player_position[0]
    player_column = player_position[1]
    direction = ""
    orientation = ""
    location = ""
    if player_row == 0:
        direction = "up"
    elif player_row == len(board) - 1:
        direction = "down"
    if player_column == 0:
        orientation = "left"
    elif player_column == len(board) - 1:
        orientation = "right"
    location += direction + " " + orientation
    return get_neighbors(player_number, player_position,
                         position, location)


def get_neighbors(player_number, player_position,
                  position, number_location=0):
    neighbors = []
    formulas = {'middle': [[-1, -1], [-1, 0], [-1, 1],
                           [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]],
                'corners': {'up left': [[0, 1], [1, 0], [1, 1]],
                            'down left': [[-1, 0], [-1, 1], [0, 1]],
                            'down right': [[-1, -1], [0, -1], [-1, 0]],
                            'up right': [[0, -1], [1, -1], [1, 0]]},
                'bounds': {'up ': [[0, -1], [1, -1], [1, 0], [1, 1], [0, 1]],
                           ' left': [[-1, 0], [-1, 1], [0, 1], [1, 0], [1, 1]],
                           'down ': [[-1, -1], [-1, 0], [-1, 1],
                                     [0, -1], [0, 1]],
                           ' right': [[-1, -1], [-1, 0], [0, -1],
                                      [1, -1], [1, 0]]}}
    formula_to_use = formulas[position]
    if isinstance(formula_to_use, type(dict())):
        formula_to_use = formula_to_use[number_location]
    for step in formula_to_use:
        neighbors.append([axis[1] + step[axis[0]] for
                          axis in enumerate(player_position)])
    return neighbors
