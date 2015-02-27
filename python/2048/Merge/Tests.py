import Merge1, Merge2, Merge3, sys
sys.path.append('../../')
import Timeutils as T

test_lists = []
list_size = 1000
list_count = 1000

line1 = [2, 0, 2, 4]
line2 = [0, 0, 2, 2]
line3 = [2, 2, 0, 0]
line4 = [2, 2, 2, 2]
line5 = [8, 16, 16, 8]
line6 = [2, 4, 4, 2, 0, 0, 2, 0, 4, 0, 4, 2]

line1result = [4, 4, 0, 0]
line2result = [4, 0, 0, 0]
line3result = [4, 0, 0, 0]
line4result = [4, 4, 0, 0]
line5result = [8, 32, 8, 0]
line6result = [2, 8, 4, 8, 2, 0, 0, 0, 0, 0, 0, 0]

# Test the merge functions

print ""
print "testing merge functions..."

assert Merge1.merge(line1) == line1result
assert Merge1.merge(line2) == line2result
assert Merge1.merge(line3) == line3result
assert Merge1.merge(line4) == line4result
assert Merge1.merge(line5) == line5result
assert Merge1.merge(line6) == line6result

assert Merge2.merge(line1) == line1result
assert Merge2.merge(line2) == line2result
assert Merge2.merge(line3) == line3result
assert Merge2.merge(line4) == line4result
assert Merge2.merge(line5) == line5result
assert Merge2.merge(line6) == line6result

assert Merge3.merge(line1) == line1result
assert Merge3.merge(line2) == line2result
assert Merge3.merge(line3) == line3result
assert Merge3.merge(line4) == line4result
assert Merge3.merge(line5) == line5result
assert Merge3.merge(line6) == line6result

print "all tests passed"
print "creating test lists..."
the_lists = T.create_lists(list_count, list_size)
print "test lists created"
print "performing tests..."

merge1times = T.runtime_lists(Merge1.merge, the_lists)
merge2times = T.runtime_lists(Merge2.merge, the_lists)
merge3times = T.runtime_lists(Merge3.merge, the_lists)

print ""
print "================="
print "Results:"
print ""
print "Merge1 total:   " + str(merge1times[0])
print "Merge1 average: " + str(merge1times[1])
print ""
print "Merge2 total:   " + str(merge2times[0])
print "Merge2 average: " + str(merge2times[1])
print ""
print "Merge3 total:   " + str(merge3times[0])
print "Merge3 average: " + str(merge3times[1])
print ""
print "================="
print ""

