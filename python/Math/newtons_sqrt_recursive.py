"""
To compute sqrt(x):
1) Start with an initial estimate y (let's pick y = 1).
2) Repeatedly improve the estimate by taking the mean of y and x/y.
Example:
Estimation Quotient              Mean
1          2 / 1 = 2             1.5     ((2 + 1) / 2)
1.5        2 / 1.5 = 1.333       1.4167  ((1.333 + 1.5) / 2)
1.4167     2 / 1.4167 = 1.4118   1.4142  ((1.4167 + 1.4118) / 2)
1.4142     ...                   ...
"""

def sqrt(x):
    """
    Calculates the square root of x, recursively.
    """
    
    def sqrt_iter(guess):
        """
        Improves the guess until it's close enough to x.
        """
        if is_good_enough(guess):
            return guess    # return the estimate if it is close enough to x

        else:
            return sqrt_iter(improve(guess)) # improve the estimate

    def is_good_enough(guess):
        """
        Is the estimate close enough? The difference of x and the square of the guess must be 
        smaller to some epsilon value to be good enough; 0.001 on this case.
        """
        return abs(guess * guess - x) / x < 0.001

    def improve(guess):
        """
        Improve the current estimate. Mean of: guess and x / guess.
        """
        return (guess + x / guess) / 2

    return sqrt_iter(1.0) # starts the recursion, using 1.0 as starting guess


