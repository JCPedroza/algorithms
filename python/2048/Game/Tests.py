import FirstTry, Benjamin, BenjaminV2, TimKautz, Anon
import Paul, Mario, LiYue
import resource

NTRIALS = 100
NMOVES = 98

def time_move(module, ntrials, nmoves):
    """ Times the move() method """
    start = resource.getrusage(resource.RUSAGE_SELF)
    Game =  module.TwentyFortyEight(10, 10)

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


print "\nTiming move() methods: "
print "FirstTry    ", time_move(FirstTry, NTRIALS, NMOVES)
print "Benjamin    ", time_move(Benjamin, NTRIALS, NMOVES)
print "BenjaminV2  ", time_move(BenjaminV2, NTRIALS, NMOVES)
print "TimKautz    ", time_move(TimKautz, NTRIALS, NMOVES)
print "Anon        ", time_move(Anon, NTRIALS, NMOVES)
print "Paul        ", time_move(Paul, NTRIALS, NMOVES)
print "Mario       ", time_move(Mario, NTRIALS, NMOVES)
print "LiYue       ", time_move(LiYue, NTRIALS, NMOVES)



print "\nTiming new_tile() methods:"
print "FirstTry    ", time_new_tile(FirstTry, NTRIALS, NMOVES)
print "Benjamin    ", time_new_tile(Benjamin, NTRIALS, NMOVES)
print "BenjaminV2  ", time_new_tile(BenjaminV2, NTRIALS, NMOVES)
print "TimKautz    ", time_new_tile(TimKautz, NTRIALS, NMOVES)
print "Anon        ", time_new_tile(Anon, NTRIALS, NMOVES)
print "Paul        ", time_new_tile(Paul, NTRIALS, NMOVES)
print "Mario       ", time_new_tile(Mario, NTRIALS, NMOVES)
print "LiYue       ", time_new_tile(LiYue, NTRIALS, NMOVES)
print
