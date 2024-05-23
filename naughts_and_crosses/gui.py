import tkinter as tk
from tkinter import messagebox


class NntGui:
    def __init__(self, master):
        self.master = master
        self.master.title("Naughts and Crosses - By Nitzan")
        label = tk.Label(self.master, text="Hello World")
        label.pack()


def main():
    root = tk.Tk()
    app = NntGui(root)
    root.mainloop()


if __name__ == "__main__":
    main()
