import time

class Clock:

    def __init__(self, *functions):
        self.functions = functions

    def __clock(self, f, range_start, range_end, repetitions):
        """
        Measures running time of a function using time.clock().
        Returns a tuple with: function name, total time, average time
        """
        start = time.clock()
        for e in range(repetitions):
            for i in range(range_start, range_end):
                f(i)
        total = time.clock() - start
        return (f.__name__ + ": ", "{:.12f}".format(total), "{:.12f}".format(total / (range_end - range_start)))

    def __run_test(self, range_start, range_end, repetitions):
        results = []
        index   = 0
        for function in self.functions:
            results.append(self.__clock(function, range_start, range_end, repetitions))
            index += 1
        return results

    def run_tests(self, test_name, range_start = 1, range_end = 1000, repetitions = 1):

        results = self.__run_test(range_start, range_end, repetitions)

        top_string = """
====================================================
Test: {0}
Range: from {1} to {2}
Repetitions: {3} 
----------------------------------------------------""".format(test_name, range_start, range_end, repetitions)
        
        total_string   = "\n\nTotal:\n"
        average_string = "\nAverage:\n"
        for i in results:
            total_string   += (i[0] + i[1] + "\n")
            average_string += (i[0] + i[2] + "\n")

        bottom_string = "\n====================================================\n\n"

        return_string = top_string + total_string + average_string + bottom_string
        
        return return_string

