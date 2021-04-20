class TicTacToe:
    def __init__(self):
        # we will use a single list to rep 3x3 board
        self.board = [' ' for _ in range(9)]
        self.current_winner = None  # keep track of winner!