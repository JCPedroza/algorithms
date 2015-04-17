"""
Monte Carlo Tic-Tac-Toe Player.

This version doesn't make use of SCORE_CURRENT and SCORE_OTHER,
squares are always scored as +1, -1, or 0.
"""

import random
import sys
sys.path.append('../../GameLogic')
import GameLogic as provided

name = "Rice"

# Constants for Monte Carlo simulator
NTRIALS = 1000       # Number of trials to run
SCORE_CURRENT = 1.0  # Score for squares played by the current player
SCORE_OTHER = 1.0    # Score for squares played by the other player
IS_REVERSE = False   # Are we playing the reverse version?

# Constants returned by board.check_win()
WIN_CONDITIONS = [provided.PLAYERO, provided.PLAYERX, provided.DRAW]


# Helper functions

def make_move(board, player):
    """
    Makes a random move in the board as the given player.
    """
    choice = random.choice(board.get_empty_squares())
    board.move(choice[0], choice[1], player)


def is_over(board):
    """
    Is the game over? (tie or player win)
    """
    return board.check_win() in WIN_CONDITIONS


# Main functions

def mc_trial(board, player):
    """
    Takes a current board and the next player to move and plays
    a complete game. The input board is converted into the
    complete game.
    """
    while not is_over(board):
        make_move(board, player)
        player = provided.switch_player(player)


def mc_update_scores(scores, board, player):
    """
    Takes a grid of scores (a list of lists) with the same
    dimensions as the Tic-Tac-Toe game, a board from a completed
    game, and which player the machine player is, then scores the
    completed board and updates the scores grid. It updates the
    score grid directly, so there is nothing to return.
    """
    winner = board.check_win()
    dim = board.get_dim()

    if winner != provided.DRAW:
        for row in range(dim):
            for column in range(dim):
                square = board.square(row, column)
                if square == winner:
                    scores[row][column] += 1
                elif square == provided.EMPTY:
                    scores[row][column] += 0
                else:
                    scores[row][column] -= 1


def get_best_move(board, scores):
    """
    Takes a current board and a grid of scores. Finds all empty
    squares with the maximum score and randomly returns one of them
    as (row, column).
    """
    empty_squares = board.get_empty_squares()
    empty_scores = [(scores[row][column], row, column) for row, column in empty_squares]
    max_value = max(empty_scores)
    return (max_value[1], max_value[2])


def mc_move(board, player, trials):
    """
    Takes a current board, which player the machine player is,
    and the number of trials to run. Uses the Monte Carlo simulation
    to return a move for the machine player in the form of a
    (row, column) tuple.
    Be sure to use the other functions you have written!
    """
    dim = board.get_dim()
    scores = [[0 for dummy_c in range(dim)] for dummy_r in range(dim)]

    for dummy_ in range(trials):
        test_board = board.clone()
        mc_trial(test_board, player)
        mc_update_scores(scores, test_board, player)

    return get_best_move(board, scores)
