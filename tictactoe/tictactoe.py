"""
Tic Tac Toe Player
"""

import math
import copy

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
    total_x = 0
    total_o = 0

    # Iterate through board and count X and O
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == X:
                total_x += 1
            elif board[i][j] == O:
                total_o += 1

    if total_x <= total_o:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions_set = set()

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                actions_set.add((i, j))
    
    return actions_set


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # Check if action is valid
    if board[action[0]][action[1]] == EMPTY:
        # Make copy of the board, get current player, and return updated board
        board_copy = copy.deepcopy(board)
        board_copy[action[0]][action[1]] == player(board)
        return board_copy
    else:
        raise Exception


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if board[0][0] and board[0][1] and board[0][2] == X or board[1][0] and board[1][1] and board[1][2] == X or board[2][0] and board[2][1] and board[2][2] == X or board[0][0] and board[1][1] and board[2][2] == X or board[0][2] and board[1][1] and board[2][0] == X:
        return X
    elif board[0][0] and board[0][1] and board[0][2] == O or board[1][0] and board[1][1] and board[1][2] == O or board[2][0] and board[2][1] and board[2][2] == O or board[0][0] and board[1][1] and board[2][2] == O or board[0][2] and board[1][1] and board[2][0] == O:
        return O
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


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
