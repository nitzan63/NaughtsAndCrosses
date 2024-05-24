import tkinter as tk


class NntGui:
    def __init__(self, master):
        self.master = master
        self.master.title("Naughts and Crosses - By Nitzan")
        self.master.geometry("400x400")
        self.master.resizable(False, False)

        self.current_turn = 1


        # create top bar:
        self.create_top_bar()

        self.update_turn_label()

    def create_top_bar(self):
        # create and pack the frame:
        top_frame = tk.Frame(self.master)
        top_frame.pack(side=tk.TOP, fill=tk.X)

        # place labels in the top bar:
        self.turn_label = tk.Label(top_frame, text="", fg="green")
        self.turn_label.pack(side=tk.LEFT)

        # set the "New Game" button:
        self.new_game_button = tk.Button(top_frame, text="New Game", command=self.reset_board)
        self.new_game_button.pack(side=tk.RIGHT)

    def reset_board(self):
        # TODO: Implement logic
        print("Resetting board")

    def update_turn_label(self):
        if self.current_turn == 1:
            self.turn_label.config(text="P1 Turn O", fg="green")
        else:
            self.turn_label.config(text="P2 Turn X", fg="red")


def main():
    root = tk.Tk()
    app = NntGui(root)
    root.mainloop()


if __name__ == "__main__":
    main()
