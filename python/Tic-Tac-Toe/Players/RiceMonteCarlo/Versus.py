import sys, RiceMonteCarlo, Tim
sys.path.append('../../GameLogic')
import GameLogic

trials = 1000
games = 10

def play_game(playerX, playerO):
    return GameLogic.play_game_versus(playerX, playerO, trials)


def play_many_games(playerA, playerB, games):
    scores = {playerA.name: 0, playerB.name: 0, "Draw": 0}
    for game in xrange(games):
        print "\r playing game {0} of {1}".format(game+1, games),
        sys.stdout.flush()
        playerA, playerB = playerB, playerA
        result = play_game(playerA, playerB)
        scores[result[1]] += 1
    return scores

print play_many_games(RiceMonteCarlo, Tim, games)