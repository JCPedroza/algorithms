/**
* To compute sqrt(x):
* 1) Start with an initial estimate y (let's pick y = 1).
* 2) Repeatedly improve the estimate by taking the mean of y and x/y.
*
* Example:
* Estimation Quotient              Mean
* 1          2 / 1 = 2             1.5     ((2 + 1) / 2)
* 1.5        2 / 1.5 = 1.333       1.4167  ((1.333 + 1.5) / 2)
* 1.4167     2 / 1.4167 = 1.4118   1.4142  ((1.4167 + 1.4118) / 2)
* 1.4142     ...                   ...
* 
*/
object NewtonsSqrt{

  /** Computes the square root of a number. */
  def sqrt(x: Double) = {
    
    /**
    * Iterative function that computes the square root of a number.
    * Will improve the estimate until it is close enough to x.
    * @param guess The initial or current estimate.
    * @param x     Computing the square root of this number.
    */
    def sqrtIter(guess: Double): Double =
      if (isGoodEnough(guess)) guess     // return the value if the estimate is good enough
      else sqrtIter(improve(guess))      // improve the estimate

    /** Computes the absolute value of a number. */
    def abs(x:Double) = if (x < 0) -x else x

    /** 
    * Is the estimate close enough? The difference of x and the square of the guess must be 
    * smaller to some epsilon value, 0.001 on this case. 
    */
    def isGoodEnough(guess: Double) =
      abs(guess * guess - x) / x < 0.001

    /** 
    * Improve the current estimate. Mean of: guess and x / guess.
    */
    def improve(guess: Double) =
      (guess + x / guess) / 2

    sqrtIter(1.0)

  }
  
}