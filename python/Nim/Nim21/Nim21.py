# -*- coding: utf-8 -*-

"""
Nim 21 game and machine players.
"""
import random


# ===============
# The Game Class
# ===============

class Nim21:
    """
    Nim 21 game.
    """
    def __init__(self, player1, player2, heaps=21):
        self._heaps = heaps
        self._player1 = player1
        self._player2 = player2
        self._winner = None

    def __str__(self):
        return "heaps: " + str(self._heaps)

    def _switch_player(self, player):
        return self._player2 if player == self._player1 else self._player1

    def get_heaps(self):
        return self._heaps

    def get_winner(self):
        return self._winner

    def remove_heaps(self, num, player):
        """
        Remove heaps from the game.
        """
        if 0 < num < 4:
            self._heaps -= num
        else:
            raise ValueError("num must be an integer greater than 0 and less than 4, \
                your input was {0}".format(num))
        if self._heaps <= 0:
            self._winner = player

    def play_game(self, verbose=False):
        """
        Plays a Nim 21 game. Moves and results will be printed if
        verbose = True.
        """
        current_player = self._player1

        while not self._winner:
            player_choice = current_player.play(self)
            self.remove_heaps(player_choice, current_player)
            if verbose:
                print "player {0} removes {1} heaps".format(current_player.get_name(), player_choice)
            current_player = self._switch_player(current_player)

        if verbose:
            print "player {0} wins!".format(self._winner.get_name())
        return self._winner

    def clone(self, player1, player2):
        """
        Creates a clone of this object.
        """
        return Nim21(player1, player2, self._heaps)


# ===============
# Players
# ===============

# Every player must have a play method, which takes a game state and retuns a move
# to make, which is the number of heaps to remove (an integer in the range [1, 3])
# and a name string.

class Player(object):
    """
    Base class for Nim 21 players.
    """
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

class MCPlayer(Player):
    """
    Monte Carlo player.
    """
    def __init__(self, name):
        super(MCPlayer, self).__init__(name)
        self._trials = 300
    
    def play(self, game_state):
        if game_state.get_heaps() < 4:    # Check if win is possible this turn
            return game_state.get_heaps()

        results = [[0, 1], [0, 2], [0, 3]]      # [games won, move (heaps to take)]
        for result in results:                  # play simulations
            for trial in xrange(self._trials):
                myself = RngPlayer("myself")
                other = RngPlayer("other")
                game = game_state.clone(other, myself)
                game.remove_heaps(result[1], myself)   # make the predefined move
                winner = game.play_game()              # then simulate a game after that move
                if winner.get_name() == "myself":
                    result[0] += 1                     # increase the score for that move if win
        return max(results)[1]                         # return the move with better score

class MinPlayer(Player):
    """
    Player that always removes one heap.
    """
    def __init__(self, name):
        super(MinPlayer, self).__init__(name)
    
    def play(self, game_state):
        return 1

class MaxPlayer(Player):
    """
    Player that always removes three heaps.
    """
    def __init__(self, name):
        super(MaxPlayer, self).__init__(name)
    
    def play(self, game_state):
        return 3

class RngPlayer(Player):
    """
    Player that removes heaps randomly.
    """
    def __init__(self, name):
        super(RngPlayer, self).__init__(name)

    def play(self, game_state):
        return random.randrange(1, 4)

class OptimalPlayer(Player):
    """
    Player that uses the optinal strategy. remove exactly enough items so that the number 
    of items remaining in the heap has remainder zero when divided by four. For example, 
    if the heap contains 10 items, you should remove 2 items to leave 8 items remaining 
    since 8 divided by 4 has remainder zero. Then, if your opponent removes n items where 
    1 ≤ n ≤ 3, you should remove 4−n items to restore heap to a state where the number of items 
    remaining has remainder zero when divided by four. Repeating this process ensures that you 
    can always remove the last item(s).
    """
    def __init__(self, name):
        super(OptimalPlayer, self).__init__(name)

    def play(self, game_state):
        if game_state.get_heaps() < 4:     # Check if win is possible this turn
            return game_state.get_heaps()

        heaps = game_state.get_heaps()
        for index in range(1, 4):
            if (heaps - index) % 4 == 0:   # Check which move leaves a board with n % 4 = 0
                return index
        return 1                           # Take one if no move was found


# ===============
# Play Area
# ===============

# Create players
player1 = MCPlayer("Smash")
player2 = OptimalPlayer("Optimal")

# Play games
ngames = 10
results = {player1.get_name(): 0, player2.get_name(): 0}
for _ in xrange(ngames):
    game = Nim21(player1, player2)
    winner = game.play_game().get_name()
    results[winner] += 1
    player1, player2 = player2, player1

# Print results
print results
