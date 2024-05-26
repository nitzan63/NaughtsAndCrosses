import tkinter as tk
import random
from gui import NncGui
from board import Board
from cell import Cell
import constants
from naughts_and_crosses.player import Player
from naughts_and_crosses.stats import Stats


class Game:
    """
    This class manages the logic of the game. It holds as attributes the board, players and statistics.
    the class keeps track of the progress of the game and handles the results.
    """
    def __init__(self):
        self.board = Board()
        self.stats = Stats()
        self.players = {
            1: Player(constants.P1, constants.P1_SYMBOL, constants.P1_COLOR),
            2: Player(constants.P2, constants.P2_SYMBOL, constants.P2_COLOR)
        }
        self.current_player = self.players[1]
        self.current_turn = 0

    def new_game(self):
        """
        Cleans the board and randomly chooses which player starts
        """
        self.board.reset()
        # choose randomly from players:
        self.current_player = self.players[random.choice(list(self.players.keys()))]
        self.current_turn = 0

    def make_move(self, row, col):
        """
        Gets the row and call from the GUI and checks for a result.
        :returns winner (int) for a winner or a draw. returns None if there is no result.
        """
        if self.board.make_move(row, col, self.current_player):
            self.current_turn += 1
            winner = self.check_result()
            if winner:
                self.stats.update_winner(winner)
                return winner
            elif self.current_turn == 9:
                self.stats.update_draws()
                return constants.DRAW
            return None
        return False

    def get_next_player(self):
        """
        calculates the next player to play (in this version only 2 players, but in a future versions there maybe more)
        :return: number of the player to play next
        """
        players_keys = list(self.players.keys())
        curr_index = players_keys.index(self.current_player.number)
        next_index = (curr_index + 1) % len(self.players)
        return self.players[players_keys[next_index]]

    def check_result(self):
        """
        checks possible winning combinations
        :return: number of winning player if there is one, or None
        """
        winning_combinations = [
            # rows:
            [self.board.get_cell_value(0, 0), self.board.get_cell_value(0, 1), self.board.get_cell_value(0, 2)],
            [self.board.get_cell_value(1, 0), self.board.get_cell_value(1, 1), self.board.get_cell_value(1, 2)],
            [self.board.get_cell_value(2, 0), self.board.get_cell_value(2, 1), self.board.get_cell_value(2, 2)],
            # cols:
            [self.board.get_cell_value(0, 0), self.board.get_cell_value(1, 0), self.board.get_cell_value(2, 0)],
            [self.board.get_cell_value(0, 1), self.board.get_cell_value(1, 1), self.board.get_cell_value(2, 1)],
            [self.board.get_cell_value(0, 2), self.board.get_cell_value(1, 2), self.board.get_cell_value(2, 2)],
            # diagonal:
            [self.board.get_cell_value(0, 0), self.board.get_cell_value(1, 1), self.board.get_cell_value(2, 2)],
            [self.board.get_cell_value(0, 2), self.board.get_cell_value(1, 1), self.board.get_cell_value(2, 0)]
        ]

        for combination in winning_combinations:
            if combination[0] is not None and combination[0] == combination[1] == combination[2]:
                return self.current_player.number
        return None

    def get_cell_value(self, row, col):
        return self.board.get_cell_value(row, col)

    def run(self):
        """
        Launches The GUI
        """
        root = tk.Tk()
        app = NncGui(root, self)
        root.mainloop()
