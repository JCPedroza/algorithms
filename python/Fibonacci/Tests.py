import sys
import Fibonacci as F
sys.path.append('../')
import Timeutils as T

init = 0
end  = 900
range_repeats = 10
single_repeats = 200

print "\nRuntime for a range of inputs: from {0} to {1}, {2} repeats:".format(init, end, range_repeats)

time_fibR = "Takes too long."
print "Recursive: ", time_fibR

time_fibTR = T.resource_runtime_range(F.fibTR, init, end, range_repeats)[0]
print "Tail Recursive:          ", time_fibTR

time_fibFR = T.resource_runtime_range(F.fibFR, init, end, range_repeats)[0]
print "For loop range():        ", time_fibFR

time_fibFX = T.resource_runtime_range(F.fibFX, init, end, range_repeats)[0]
print "For loop xrange():       ", time_fibFX

time_fibFN = T.resource_runtime_range(F.fibFN, init, end, range_repeats)[0]
print "For loop numpy.arange(): ", time_fibFN

time_fibAnalytic = T.resource_runtime_range(F.fibAnalytic, init, end, range_repeats)[0]
print "Analytic:                ", time_fibAnalytic

time_fibMatrix = T.resource_runtime_range(F.fibMatrix, init, end, range_repeats)[0]
print "Matrix:                  ", time_fibMatrix

time_fibLSR = T.resource_runtime_range(F.fibLSR, init, end, range_repeats)[0]
print "Large Step Recurrence:   ", time_fibLSR




print "\nRuntime for constant input {0}, {1} repeats: ".format(end, single_repeats)
time_fibR = "Takes too long."
print "Recursive: ", time_fibR

time_fibTR = T.resource_runtime(F.fibTR, end, single_repeats)[0]
print "Tail Recursive:          ", time_fibTR

time_fibFR = T.resource_runtime(F.fibFR, end, single_repeats)[0]
print "For loop range():        ", time_fibFR

time_fibFX = T.resource_runtime(F.fibFX, end, single_repeats)[0]
print "For loop xrange():       ", time_fibFX

time_fibFN = T.resource_runtime(F.fibFN, end, single_repeats)[0]
print "For loop numpy.arange(): ", time_fibFN

time_fibAnalytic = T.resource_runtime(F.fibAnalytic, end, single_repeats)[0]
print "Analytic:                ", time_fibAnalytic

time_fibMatrix = T.resource_runtime(F.fibMatrix, end, single_repeats)[0]
print "Matrix:                  ", time_fibMatrix

time_fibLSR = T.resource_runtime(F.fibLSR, end, single_repeats)[0]
print "Large Step Recurrence:   ", time_fibLSR



