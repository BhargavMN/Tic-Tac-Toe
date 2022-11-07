"""
Tic Tac Toe Player
"""
import copy
import math

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
    counter_o = 0
    counter_x= 0

    for row in board:
        for cell in row:
            if cell == 'X':
                counter_x += 1
            if cell == "O":
                counter_o += 1

    return X if counter_x == counter_o else O


def actions(board):

    """
    Returns set of all possible actions (i, j) available on the board.
    """
    action_set = set()

    for row in range(3):
        for coll in range(3):
            if board[row][coll] == EMPTY:
                action_set.add((row, coll))

    return action_set


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    i, j = action

    if i not in range(3) or j not in range(3):
        raise ValueError('Invalid Co-ordinates')
    if board[i][j] != EMPTY:
        raise ValueError('Non-empty Co-ordinates')
    board_copy = copy.deepcopy(board)
    board_copy[i][j] = player(board)

    return board_copy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][2] != EMPTY:
            return board[i][0]
        if board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[2][i] != EMPTY:
            return board[0][i]
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[2][2] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[2][0] != EMPTY:
        return board[0][0]
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    for row in range(3):
        for coll in range(3):
            if board[row][coll] == EMPTY:
                return

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
