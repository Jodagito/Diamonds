class Neighbors:
    board = []
    player = ""
    player_number = 0
    player_position = []
    player_row = 0
    player_column = 0
    board_bounds = 0

    def __init__(self, board, player, player_number, player_position):
        self.board = board
        self.player = player
        self.player_number = player_number
        self.player_position = player_position
        self.player_row = player_position[0]
        self.player_column = player_position[1]
        self.board_bounds = len(board) - 1

    def update_attributes(self, board, player, player_number, player_position):
        self.board = board
        self.player = player
        self.player_number = player_number
        self.player_position = player_position
        self.player_row = player_position[0]
        self.player_column = player_position[1]
        self.board_bounds = len(board) - 1

    def get_number_position(self):
        if self.player_row in [0, self.board_bounds] and self.player_column in [0, self.board_bounds]:
            return "corners"
        elif (self.player_row not in [0, self.board_bounds] and
              self.player_column not in [0, self.board_bounds]):
            return "middle"
        else:
            return "bounds"

    def get_orientation(self):
        vertical_orientation = ""
        horizontal_orientation = ""
        if self.player_row == 0:
            vertical_orientation = "up"
        elif self.player_row == self.board_bounds:
            vertical_orientation = "down"
        if self.player_column == 0:
            horizontal_orientation = "left"
        elif self.player_column == self.board_bounds:
            horizontal_orientation = "right"
        return vertical_orientation + " " + horizontal_orientation

    def select_distance_formula(self, position, number_location=0):
        distance_formulas = {'middle': [[-1, -1], [-1, 0], [-1, 1],
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
        formula_to_use = distance_formulas[position]
        if isinstance(formula_to_use, type(dict())):
            formula_to_use = formula_to_use[number_location]
        return formula_to_use

    def get_neighbors(self, formula_to_use):
        neighbors = []
        for neighbor_distance in formula_to_use:
            neighbor_coordinates = [position_axis[1] + neighbor_distance[position_axis[0]] for
                                    position_axis in enumerate(self.player_position)]
            neighbors.append(neighbor_coordinates)
        return neighbors
