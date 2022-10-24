import tkinter as tk
from tkinter import font
from game import *


class TicTacToeGUI(tk.Tk):
    def __init__(self, game):
        super().__init__()
        self.title = "Tic-Tac-Toe Board"
        self._cells = {}
        self.game = game
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
        for row in range(self.game.board_size):
            self.rowconfigure(row, weight=1, minsize=50)
            self.columnconfigure(row, weight=1, minsize=75)
            for column in range(self.game.board_size):
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
                button.bind("<ButtonPress-1>", self.play)
                button.grid(
                    row=row,
                    column=column,
                    padx=5,
                    pady=5,
                    sticky="nsew"
                )
    def play(self, event):
        clicked_button = event.widget
        row, col = self._cells[clicked_button]
        move = Move(row, col, self.game.current_player.label)
        if self.game.is_valid_move(move):
            self._update_button(clicked_button)
            self.game.process_move(move)
            if self.game.is_tie():
                self._update_display(msg="Tied game!", color="red")
            elif self.game.has_winner():
                self._highlight_cells()
                msg = f'Player "{self.game.current_player.label}" won!'
                color = self.game.current_player.color
                self._update_display(msg, color)
            else:
                self.game.toggle_player()
                msg = f"{self.game.current_player.label}'s turn"
                self._update_display(msg)
    
    def _update_button(self, clicked_btn):
        clicked_btn.config(text=self.game.current_player.label)
        clicked_btn.config(fg=self.game.current_player.color)
    
    def _update_display(self, msg, color="black"):
        self.display["text"] = msg
        self.display["fg"] = color
    
    def _highlight_cells(self):
        for button, coordinates in self._cells.items():
            if coordinates in self.game.winner_combo:
                button.config(highlightbackground="red")


def main():
    """Create the game's board and run its main loop."""
    game = TicTacToeGame()
    board = TicTacToeGUI(game)
    board.mainloop()

if __name__ == "__main__":
    main()