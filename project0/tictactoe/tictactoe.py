"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    # It is assumed that 'X' plays first, and the mode always
    # alternates.
    # The function follows the logic of the count of current
    # None values,
    # if count is odd, 'X' plays,
    # if count is even, 'O' plays.

    # Initialize count
    count = 0
    for row in board:
        count += row.count(None)
    if count % 2 == 0:
        return O
    return X
    # raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == None:
                actions.append((i, j))
    return actions
    # raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # Unpack the action
    i, j = action
    board_copy = deepcopy(board)
    # error handling
    if not (0 <= i <= 2 and 0 <= j <= 2):
        raise ValueError("Invalid Board Position")
    if board_copy[i][j] != None:
        raise ValueError("Board Position Occupied")
    board_copy[i][j] = player(board)

    return board_copy
    # raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    for mark in 'XO':
        if is_win(mark, board):
            return mark
    return None
    # raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # Check if the game has been won
    if winner(board) != None:
        return True

    # Check if all cells are filled
    count = 0
    for row in board:
        count += row.count(None)
    if count == 0:
        return True
    else:
        # Game still in progress
        return False
    # raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError

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
