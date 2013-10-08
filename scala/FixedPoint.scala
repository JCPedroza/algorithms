import math.abs

/**
* Calculates the fixed point of a function. 
*
* A number x is called a fixed point of a function f if f(x) = f
*
* For some functions f we can locate the fixed points by starting with an initial
* estimate and then by applying f in a repetitive way:
* x, f(x), f(f(x)), f(f(f(x))), ...
* Until the value does not vary anymore (or the change is sufficiently small).
* 
* Example: 
* fixedPoint(<function>)(<initial guess>)
* fixedPoint(x => 1 + x / 2)(1) 
*
* Average Damp:
*
* Sometimes we need to take averages to dampen the oscillations. Here is an example:
* The specification of a square root function:
* sqrt(x) = the number y such that y * y = x
* Or by dividing both sides of the equetion by y:
* sqrt(x) = the number y such that y = x / y
* Consequently, sqrt(x) is a fixed point of the function (y => x / y).
* 
* This suggests to calculate sqrt(x) by iteration towads a fixed point:
* def sqrt(x: Double) = fixedPoint(y => x / y)(1.0)
* Unfortunately, this does not converge. If you print the guess value in the iterate function, 
* you will notice that sqrt(x) enters an infinite loop, oscillating between two values.
*
* One way to control such oscillations is to prevent the estimation from varying too much. This 
* is done by averaging successive values of the original sequence. So for example, in sqrt(2)
* instead of oscilating between values 1 and 2, it averages them to 1.5, setting the path to 
* convergence. sqrt(2) using average damp would produce, insead of 1, 2, 1, 2 ... :
* 1.5
* 1.41666666...
* ...
* 1.41421356...
*
* For that reason, we can use average damping to calculate the fixed point of a function.
* With that in mind, we can define sqrt() as:
* def sqrt(x: Double) = fixedPoint(averageDamp(y => x / y))(1)
* As opposed to:
* def sqrt(x: Double) = fixedPoint(y => x / y)(1)
*
*/
object FixedPoint extends App{
  val tolerance = 0.0001                      // tolerance reference for isCloseEnough                    
  def isCloseEnough(x: Double, y: Double) =   // is the estimate close enough?
    abs(x-y) < tolerance * abs(x)  
  /** Calculates the fixed point of a function */            
  def fixedPoint(f: Double => Double)(firstGuess:Double) = {
    def iterate(guess: Double): Double = {
      val next = f(guess)
      if (isCloseEnough(guess, next)) next    // return value if it's close enough
      else iterate(next)                      // apply the function again if it's not -
    }                                         // close enough
    iterate(firstGuess)                       // start of recursion with initial guess
  }
  
  /** To apply average damp if needed (see object notes) */
  def averageDamp(f: Double => Double)(x: Double) = (x + f(x)) / 2

}