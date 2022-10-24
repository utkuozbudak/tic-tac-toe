import tkinter as tk
from tkinter import font


class TicTacToeGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title = "Tic-Tac-Toe Board"
        self._cells = {}
        self._create_board_display()
        self._create_board_grid()
    
    def _create_board_display(self):
        frame = tk.Frame(master=self)
        frame.pack(fill=tk.X)
        self.display = tk.Label(
            master=frame,
            text = "Ready?",
            font = font.Font(size=30, weight="bold")
        )
        self.display.pack()
    
    def _create_board_grid(self):
        grid_frame = tk.Frame(master=self)
        grid_frame.pack()
        for row in range(3):
            self.rowconfigure(row, weight=1, minsize=50)
            self.columnconfigure(row, weight=1, minsize=75)
            for column in range(3):
                button = tk.Button(
                    master=grid_frame,
                    text="",
                    font = font.Font(size=36, weight="bold"),
                    fg="black",
                    width=3,
                    height=2,
                    highlightbackground="lightblue"
                )
                self._cells[button] = (row, column)
                button.grid(
                    row=row,
                    column=column,
                    padx=5,
                    pady=5,
                    sticky="nsew"
                )


def main():
    """Create the game's board and run its main loop."""
    board = TicTacToeGUI()
    board.mainloop()

if __name__ == "__main__":
    main()
    