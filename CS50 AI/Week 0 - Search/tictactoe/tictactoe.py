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
    # Create counters to record the number of moves a player has made
    x_turns = 0
    o_turns = 0

    # Iterate over each cell in the board and track how many moves each player has made
    for row in board:
        for cell in row:
            if cell == X:
                x_turns += 1
            elif cell == O:
                o_turns += 1

    # X always goes first, so if no moves have been made yet, we know it is X's turn
    if x_turns == 0:
        return X
    elif x_turns == o_turns:
        return X
    elif x_turns > o_turns:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    # Create a set to record all possible actions/moves
    possible_actions = set()

    # Iterate over each cell in the board and add the co-ordinates of empty cells to the 'possible_actions' set
    for x, row in enumerate(board):
        for y, cell in enumerate(row):
            if cell == EMPTY:
                co_ordinates = (x, y)
                possible_actions.add(co_ordinates)

    # Return possible actions if there are any, otherwise return None
    if possible_actions:
        return possible_actions
    else:
        return None


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # Call player function to determine who's move it is
    current_player = player(board)

    # Call our 'actions' function to return a set with all possible moves
    possible_actions = actions(board)

    # If the proposed move is not valid/possible, raise an exception
    if action not in possible_actions:
        raise ValueError("Invalid Action")
    # Otherwise return a copy of the board with the proposed action executed
    else:
        copy_board = copy.deepcopy(board)
        (x,y) = action
        copy_board[x][y] = current_player

    return copy_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check for horizontal wins
    for row in board:
        if row == [X, X, X]:
            return X
        if row == [O, O, O]:
            return O
    
    # Check for X vertical win
    if board[0][0] == X and board[1][0] == X and board [2][0] == X:
        return X
    elif board[0][1] == X and board[1][1] == X and board [2][1] == X:
        return X
    elif board[0][2] == X and board[1][2] == X and board [2][2] == X:
        return X

    # Check for O vertical win
    elif board[0][0] == O and board[1][0] == O and board [2][0] == O:
        return O
    elif board[0][1] == O and board[1][1] == O and board [2][1] == O:
        return O
    elif board[0][2] == O and board[1][2] == O and board [2][2] == O:
        return O

    # Check for X diagonal win
    elif board[0][0] == X and board[1][1] == X and board [2][2] == X:
        return X
    elif board[0][2] == X and board[1][1] == X and board [2][0] == X:
        return X
    
    # Check for O diagonal win
    elif board[0][0] == O and board[1][1] == O and board [2][2] == O:
        return O
    elif board[0][2] == O and board[1][1] == O and board [2][0] == O:
        return O
    
    # Otherwise, there is no winner, so return None
    else:
        return None



def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # If there is a winner, or if there are no actions remaining, the game is over; return True. Otherwise return False
    if winner(board) or not actions(board):
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    victor = winner(board)

    if victor == X:
        return 1
    elif victor == O:
        return -1
    else:
        return 0

def min_value(board):
    """
    Returns the minimum value possible from a given board
    """

    v = math.inf

    if terminal(board):
        return utility(board)

    possible_actions = actions(board)

    for action in possible_actions:
        x = (max_value(result(board, action)))
        if x < v:
            v = x
    return v


def max_value(board):
    """
    Returns the maximum value possible from a given board
    """

    v = -math.inf

    if terminal(board):
        return utility(board)

    possible_actions = actions(board)


    for action in possible_actions:
        x = (min_value(result(board, action)))
        if x > v:
            v = x

    return v

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    # Check if board is terminal, return None if so
    is_terminal = terminal(board)
    if is_terminal:
        return None

    # Check who the current player is
    current_player = player(board)
    
    if current_player == X:
        v = -math.inf
        possible_actions = actions(board)
        for action in possible_actions:
            min = min_value(result(board,action))
            if min > v:
                v = min
                move = action
        return move


    else:
        v = math.inf
        possible_actions = actions(board)
        for action in possible_actions:
            max = max_value(result(board, action))
            if max < v:
                v = max
                move = action
        return move
        


