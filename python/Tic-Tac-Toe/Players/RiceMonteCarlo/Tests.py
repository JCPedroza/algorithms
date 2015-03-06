"""
Tests for the RiceMonteCarlo Tic-Tac-Toe machine player.
"""

import RiceMonteCarlo, sys
sys.path.append('../../GameLogic')
import GameLogic

NTRIALS = RiceMonteCarlo.NTRIALS
mc_move = RiceMonteCarlo.mc_move

PLAYERX = GameLogic.PLAYERX
PLAYERO = GameLogic.PLAYERO
DRAW = GameLogic.DRAW
play_game = GameLogic.play_game

result_str = {DRAW: "draw", PLAYERX: "X", PLAYERO: "O"}

def play_a_game():
    """
    This machine player plays a game against itself, printing each move.
    """
    play_game(mc_move, NTRIALS, False, True) 


def result_test(iterations, ntrials, console_print=False):
    """
    Runs games and reports results.
    """
    results = {PLAYERX: 0, PLAYERO: 0, DRAW: 0}
    if console_print:
        print "\n============================="
        print "performing tests for ntrials {0}".format(ntrials)
    for i in range(iterations):
        result = play_game(mc_move, ntrials)
        results[result] += 1
        if console_print:
            print "performed test {0} of {1} with result {2}".format(i+1, iterations, result_str[result])
    return results

def test_ntrials(start, end, stride, iterations):
    """
    Runs tests with different ntrials values. 
    """
    results = []
    for ntrials in range(start, end, stride):
        results.append([ntrials, result_test(iterations, ntrials, True)])
    return results


# the_results = test_ntrials(2000, 2100, 200, 200)
# print the_results
play_a_game()