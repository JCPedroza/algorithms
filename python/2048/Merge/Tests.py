import Anon, Benjamin, LiYue
import sys
sys.path.append('../../')
import Timeutils as T

modules = [Anon, Benjamin, LiYue]

test_lists = []
list_size = 1000
list_count = 1000

line1 = [2, 0, 2, 4,]
line2 = [0, 0, 2, 2]
line3 = [2, 2, 0, 0]
line4 = [2, 2, 2, 2]
line5 = [8, 16, 16, 8]
line6 = [2, 4, 4, 2, 0, 0, 2, 0, 4, 0, 4, 2]
lines = [line1, line2, line3, line4, line5, line6]

line1result = [4, 4, 0, 0]
line2result = [4, 0, 0, 0]
line3result = [4, 0, 0, 0]
line4result = [4, 4, 0, 0]
line5result = [8, 32, 8, 0]
line6result = [2, 8, 4, 8, 2, 0, 0, 0, 0, 0, 0, 0]
results = [line1result, line2result, line3result, line4result, line5result, line6result]


# Test the merge functions

print ""
print "testing merge functions..."

for module in modules:
    for i in range(len(lines)):
        assert module.merge(lines[i]) == results[i]

print "all tests passed"
print "creating test lists..."
the_lists = T.create_lists(list_count, list_size)
print "test lists created"
print "performing time measurements..."

anontimes     = T.runtime_lists(Anon.merge, the_lists)
benjamintimes = T.runtime_lists(Benjamin.merge, the_lists)
liyuetimes    = T.runtime_lists(LiYue.merge, the_lists)

print ""
print "================="
print "Results:"
print ""
print "Anon total:       " + str(anontimes[0])
print "Anon average:     " + str(anontimes[1])
print ""
print "Benjamin total:   " + str(benjamintimes[0])
print "Benjamin average: " + str(benjamintimes[1])
print ""
print "LiYue total:      " + str(liyuetimes[0])
print "LiYue average:    " + str(liyuetimes[1])
print ""
print ""

print "================="
print ""

