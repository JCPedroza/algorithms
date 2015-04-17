"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
import sys
sys.path.append('../../GameLogic')
import GameLogic as provided

name = "Tim"

# Constants for Monte Carlo simulator
NTRIALS = 1000        # Number of trials to run
SCORE_CURRENT = 1.0   # Score for squares played by the current player
SCORE_OTHER = 1.0     # Score for squares played by the other player


# Add your functions here.
def mc_trial(board, player):
    """
    The function should play a game starting with the given player by making random moves, alternating between players.
    The function should return when the game is over.
    """

    while True:
        # Pick a random empty square.
        row, col = random.choice(board.get_empty_squares())
        # Mark the square with the current player.
        board.move(row, col, player)
        # Check if the player has won. If he did we break here.
        if board.check_win():
            break
        # Change player.
        player = provided.switch_player(player)


def mc_update_scores(scores, board, player):
    """
    This function takes a grid of scores (a list of lists) with the same dimensions as the Tic-Tac-Toe board, a board
    from a completed game, and which player the machine player is. The function should score the completed board and
    update the scores grid.
    """

    # Set up helper vars.
    grid = range(board.get_dim())
    winner = board.check_win()

    # If the game ended in a draw we don't update the scores.
    if winner == provided.DRAW:
        return

    # Iterate over the board and update scores.
    for col in grid:
        for row in grid:
            square = board.square(row, col)
            # Add 0 if this square is empty.
            if square == provided.EMPTY:
                continue
            # Add 1 if this square belongs to the winner.
            elif square == winner:
                scores[row][col] += 1
            # Subtract 1 if this square belongs to the loser.
            else:
                scores[row][col] -= 1


def get_best_move(board, scores):
    """
    This function should find all of the empty squares with the maximum score and randomly return one of them as a
    (row, column) tuple. It is an error to call this function with a board that has no empty squares
    (there is no possible next move), so your function may do whatever it wants in that case.
    """

    # Get free squares.
    free_squares = board.get_empty_squares()

    # If there are no free squares return here.
    if not free_squares:
        return

    # Create a dict of scores with each free square as key.
    free_scores = dict(((row, col), scores[row][col]) for row, col in free_squares)

    # Get the highest score.
    max_score = max(free_scores.values())

    # Iterate over free_scores and add all squares with the highest value to moves.
    moves = [key for key, val in free_scores.items() if val == max_score]

    # Return a random move.
    return random.choice(moves)


def mc_move(board, player, trials):
    """
    This function takes a current board, which player the machine player is, and the number of trials to run.
    The function should use the Monte Carlo simulation described above to return a move for the machine player in the
    form of a (row, column) tuple.
    """
    # Set up helper vars.
    grid = range(board.get_dim())
    score_board = [[0 for dummy_col in grid] for dummy_row in grid]

    # Run trials and update scores for best moves.
    for _ in range(trials):
        clone_board = board.clone()
        mc_trial(clone_board, player)
        mc_update_scores(score_board, clone_board, player)

    return get_best_move(board, score_board)
