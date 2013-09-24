/**
* Tail recursion implementation of the factorial algorithm. 
*
* Tail recursion:
* If a function calls itself as its last action, the function's stack frame can be reused. 
* This is called tail recursion. A tail recursive function execute at constant stack space, 
* it's really just another formulation of an iterative process. A tail recursive function is
* the functional form of a loop, and it executes just as efficiently as a loop. 
*
* This is the normal implementation of factorial:
*   def factorial(n: Int): Int = 
*     if (n == 0) 1 else n * factorial(n - 1)
*
* The normal, simpler, factorial algorithm is not tail recursive because its last action is not
* a call to itself, but a multiplication of the call to itself and n. The values of n need to be
* saved until the end,  the expression gets bigger and bigger with each recursive call, until the 
* end when it's finally reduced to the final value. 
* 
*/
object FactorialTR{

  /** Computes factorial of n, using tail recursion */
  def factorial(n: Int): Int = {
    // acc will store the result of the multiplication on each iteration
    def loop(acc: Int, n: Int): Int =
      if (n == 0) acc
      else loop(acc * n, n - 1)
    loop(1, n)
  }
}