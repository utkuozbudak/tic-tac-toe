import enum
from itertools import cycle
from typing import NamedTuple


class Player(NamedTuple):
    label: str
    color: str

class Move(NamedTuple):
    row: int
    column: int
    label: str = ""

BOARD_SIZE = 3
DEFAULT_PLAYERS = (
    Player(label="X", color="blue"),
    Player(label="O", color="green"),
)

class TicTacToeGame():
    def __init__(self, players=DEFAULT_PLAYERS, board_size=BOARD_SIZE):
        """ Constructor.

        Args:
            players (Player, optional): Players objects. Defaults to DEFAULT_PLAYERS.
            board_size (int, optional): Size of the game board. Defaults to BOARD_SIZE.
        """
        self.players = cycle(players)
        self.board_size = board_size
        self.current_player = next(self.players)
        self.winner_combo = []
        self.current_moves = []
        self._has_winner = False
        self.winning_combos = []
        self._setup_board()
        self.deneme = "abc"
        self._deneme = "abc1"
    
    def _setup_board(self):
        self._current_moves = [
            [Move(row, col) for col in range(self.board_size)]
            for row in range(self.board_size)
        ]
        self._winning_combos = self._get_winning_combos()
    
    def _get_winning_combos(self):
        """ 
        Find the game winning combinations.
        """
        rows = [
            [(move.row, move.column) for move in row]
            for row in self._current_moves
        ]
        columns = [list(col) for col in zip(*rows)]
        first_diagonal = [row[i] for i, row in enumerate(rows)]
        second_diagonal = [column[j] for j, column in enumerate(reversed(columns))]
        return rows + columns + [first_diagonal, second_diagonal]
    
    def is_valid_move(self, move):
        """ Check if a move is valid.

        Args:
            move (Move): Currently played Move.

        Returns:
            bool: return true if there is no winner and move is played on an empty cell. Else return false.
        """
        row, col = move.row, move.column
        is_move_played = self._current_moves[row][col].label == ""
        is_winner = not self._has_winner
        return is_winner and is_move_played
    
    def process_move(self, move):
        """ Processing of the move.

        Args:
            move (Move): Currently player Move.
        """
        row, col = move.row, move.column
        self._current_moves[row][col] = move
        for combo in self._winning_combos:
            results = set(
                self._current_moves[n][m].label
                for n, m in combo
            )
            is_win = (len(results) == 1) and ("" not in results)
            if is_win:
                self._has_winner = True
                self.winner_combo = combo
                break
    
    def has_winner(self):
        return self._has_winner
    
    def is_tie(self):
        """ Check if there is a tie.

        Returns:
            bool: returns true if there is no winner and there is no any cells left to play.
        """
        no_winner = not self._has_winner
        played_moves = (
            move.label for row in self._current_moves for move in row
        )
        return no_winner and all(played_moves)
    
    def toggle_player(self):
        """
        Toggle to the next player for the next move.
        """
        self.current_player = next(self.players)