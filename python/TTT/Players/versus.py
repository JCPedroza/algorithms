import sys
# players
import minimax
import tim
import ricemc
# game logic
sys.path.append('/../GameLogic')
import gamelogic

TRIALS = 100    # trials for montecarlo players
GAMES = 10      # games to be played


def play_game(playerX, playerO):
    return gamelogic.play_game_versus(playerX, playerO, TRIALS)


def play_many_games(playerA, playerB, games):
    scores = {playerA.name: 0, playerB.name: 0, "Draw": 0}
    for game in xrange(games):
        print "\r playing game {0} of {1}".format(game+1, games),
        sys.stdout.flush()
        playerA, playerB = playerB, playerA
        result = play_game(playerA, playerB)
        scores[result[1]] += 1
    return scores


print play_many_games(ricemc, tim, GAMES)
