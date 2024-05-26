import tkinter as tk
import random
from gui import NncGui
from board import Board
from cell import Cell
import constants
from naughts_and_crosses.player import Player
from naughts_and_crosses.stats import Stats


class Game:
    def __init__(self):
        self.board = Board()
        self.stats = Stats()
        self.players = {
            1: Player(constants.P1, constants.P1_SYMBOL, constants.P1_COLOR),
            2: Player(constants.P2, constants.P2_SYMBOL, constants.P2_COLOR)
        }
        self.current_player = self.players[1]
        self.current_turn = 0

    def reset_game(self):
        self.board.reset()
        # choose randomly from players:
        self.current_player = self.players[random.choice(list(self.players.keys()))]
        self.current_turn = 0

    def make_move(self, row, col):
        if self.board.make_move(row, col, self.current_player):
            self.current_turn += 1
            self.current_player = self.get_next_player()
            return True
        return False

    def get_next_player(self):
        players_keys = list(self.players.keys())
        curr_index = players_keys.index(self.current_player.number)
        next_index = (curr_index + 1) % len(self.players)
        return self.players[players_keys[next_index]]


    def get_cell_value(self, row, col):
        return self.board.get_cell_value(row, col)

    def run(self):
        root = tk.Tk()
        app = NncGui(root, self)
        root.mainloop()



