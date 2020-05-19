# Utility functions

def is_win(mark, board):
    """Checks if the current configuration is a win or tie."""
    return (mark == board[0][0] == board[0][1] == board[0][2] or # row 0
            mark == board[1][0] == board[1][1] == board[1][2] or # row 1
            mark == board[2][0] == board[2][1] == board[2][2] or # row 2
            mark == board[0][0] == board[1][0] == board[2][0] or # column 0
            mark == board[0][1] == board[1][1] == board[2][1] or # column 1
            mark == board[0][2] == board[1][2] == board[2][2] or # column 2
            mark == board[0][0] == board[1][1] == board[2][2] or # diagonal
            mark == board[0][2] == board[1][1] == board[2][0]) # rev diag
