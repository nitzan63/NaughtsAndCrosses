import tkinter as tk


class NncGui:
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

        # update turn label:
        self.update_turn_label()

    def create_top_bar(self):
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

    def reset_board(self):
        self.game.reset_game()
        for row in self.buttons:
            for button in row:
                button.config(text="", state=tk.NORMAL)
        self.update_turn_label()

    def handle_click(self, row, col):
        player = self.game.current_player
        if self.game.make_move(row, col):
            value = self.game.get_cell_value(row, col)
            self.buttons[row][col].config(text=value, fg=player.color)
            self.update_turn_label()
            # TODO: implement end game logic

    def update_turn_label(self):
        player = self.game.current_player
        self.turn_label.config(text=f"P{player.number} Turn {player.symbol}", fg=player.color)
