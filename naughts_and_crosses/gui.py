import tkinter as tk
from tkinter import messagebox

from naughts_and_crosses import constants


class NncGui:
    """
    This class manages the GUI interface for the game. It's responsible for the input from the user, and displays the board.
    """
    def __init__(self, master, game):
        self.master = master
        self.game = game
        self.master.title("Naughts and Crosses - By Nitzan")
        self.master.geometry("400x400")
        self.master.resizable(False, False)

        # initialize attributes:
        self.turn_label = None
        self.new_game_button = None
        self.board_frame = None
        self.buttons = []

        # create top bar:
        self.create_top_bar()

        # create game board:
        self.create_game_board()

        # create stats bar:
        self.create_stats_bar()

        # update turn label:
        self.update_turn_label()

    def create_top_bar(self):
        """
        Creates the top bar of the game screen
        """
        # create and pack the frame:
        top_frame = tk.Frame(self.master)
        top_frame.pack(side=tk.TOP, fill=tk.X)

        # place labels in the top bar:
        self.turn_label = tk.Label(top_frame, text="", fg="black", font=("Helvetica", 24))
        self.turn_label.pack(side=tk.LEFT)

        # set the "New Game" button:
        self.new_game_button = tk.Button(top_frame, text="New Game", font=("Helvetica", 24), command=self.reset_board)
        self.new_game_button.pack(side=tk.RIGHT)

    def create_game_board(self):
        """
        Creates the game board of the game
        :return:
        """
        self.board_frame = tk.Frame(self.master)
        self.board_frame.pack(expand=True)

        for row in range(3):
            row_buttons = []
            for col in range(3):
                button = tk.Button(self.board_frame, text="", font=("Arial", 24), width=5, height=2,
                                   command=lambda r=row, c=col: self.handle_click(r, c))
                button.grid(row=row, column=col)
                row_buttons.append(button)
            self.buttons.append(row_buttons)

    def create_stats_bar(self):
        """
        Creates the stats bar of the game screen
        :return:
        """
        bottom_frame = tk.Frame(self.master)
        bottom_frame.pack(side=tk.BOTTOM, fill=tk.X)

        self.stats_label = tk.Label(bottom_frame, text="", font=("Helvetica", 20))
        self.stats_label.pack(side=tk.LEFT)

        self.reset_stats_button = tk.Button(bottom_frame, text="Reset Game", font=("Helvetica", 24),
                                            command=self.reset_stats)
        self.reset_stats_button.pack(side=tk.RIGHT)

        self.update_stats_label()

    def reset_stats(self):
        """
        Resets the stats bar of the game screen
        """
        self.game.stats.reset()
        self.reset_board()
        self.update_stats_label()

    def reset_board(self):
        """
        Resets the game board and enables all buttons
        """
        self.game.new_game()
        for row in self.buttons:
            for button in row:
                button.config(text="", state=tk.NORMAL)
        self.update_turn_label()

    def handle_click(self, row, col):
        """
        Handles the click of the board button.
        after the player clicks the board button, the GUI asks the game class for the result.
        if the result is not false (which means the player pressed a valid cell button), this method will update the game board.
        if the result is a number, it will ask to declare the results and disable all buttons.
        else -> displays next players turn
        """
        try:
            result = self.game.make_move(row, col)
            if result is not False:
                value = self.game.get_cell_value(row, col)
                player = self.game.current_player
                self.buttons[row][col].config(text=value, fg=player.color)
                if result == constants.DRAW or result is not None:
                    self.declare_result(result)
                    self.disable_board_buttons()
                else:
                    self.game.current_player = self.game.get_next_player()
                    self.update_turn_label()
                self.update_stats_label()
        except Exception as e:
            messagebox.showerror("ERROR", f"Error handling click at {row},{col}: {e}")

    def declare_result(self, result):
        """
        Declares the result of the game based on the result
        """
        if result == constants.DRAW:
            message = "It's a Draw!"
        else:
            message = f"Player {result} Won!"
        message += "\n Press New Game button for another round!"
        messagebox.showinfo("Game Over", message)

    def update_turn_label(self):
        player = self.game.current_player
        self.turn_label.config(text=f"Player {player.number}'s Turn {player.symbol}\n"
                                    f"Choose a cell", fg=player.color)

    def update_stats_label(self):
        stats = self.game.stats
        stats_text = (
            f"P1 Score: {stats.p1_score}\n"
            f"P2 Score: {stats.p2_score}\n"
            f"Draws: {stats.draws}\n"
            f"Games Played: {stats.games_played}\n"
        )

        self.stats_label.config(text=stats_text)

    def disable_board_buttons(self):
        """
        disable all buttons after the game is over
        """
        for row in self.buttons:
            for button in row:
                button.config(state=tk.DISABLED)
