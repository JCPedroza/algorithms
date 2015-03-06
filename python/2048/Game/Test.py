import FirstTry, Another2048, sys, resource
sys.path.append('../../')
import Timeutils

NTRIALS = 100
NMOVES = 98

def time_move(module, ntrials, nmoves):
    """ Times the move() method """
    start = resource.getrusage(resource.RUSAGE_SELF)
    Game =  module.TwentyFortyEight(4, 4)

    for i in range(ntrials):
        Game.reset()
        for j in range(1, nmoves + 1):
            Game.move(i % 4 + 1)

    end = resource.getrusage(resource.RUSAGE_SELF)
    return end.ru_utime - start.ru_utime

def time_new_tile(module, ntrials, times):
    """ Times the new_tile() method """
    start = resource.getrusage(resource.RUSAGE_SELF)
    Game =  module.TwentyFortyEight(10, 10)

    for i in range(ntrials):
        Game.reset()
        for j in range(times):
            Game.new_tile()

    end = resource.getrusage(resource.RUSAGE_SELF)
    return end.ru_utime - start.ru_utime


print
print "FirstTry move(): ", time_move(FirstTry, NTRIALS, NMOVES)
print "Another  move(): ", time_move(Another2048, NTRIALS, NMOVES)
print
print "FirstTry new_tile(): ", time_new_tile(FirstTry, NTRIALS, NMOVES)
print "Another  new_tile(): ", time_new_tile(Another2048, NTRIALS, NMOVES)
print

# TestGame = FirstTry.TwentyFortyEight(4, 4)
# TestGame.new_tile()
# TestGame = FirstTry.TwentyFortyEight(10, 10)
# TestGame.new_tile()