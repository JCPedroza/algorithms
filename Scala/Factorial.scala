object Factorial{

  /** Computes factorial of n. */
  def factorialRecursive(n: Int): Int = 
    if (n < 1) 1 else n * factorialRecursive(n - 1)
  
  /** Computes factorial of n using tail recursion */
  def factorialTailRecursive(n: Int): Int = {
    def recursion(n: Int, acc: Int): Int = 
      if (n < 1) acc else recursion(n - 1, acc * n)
    recursion(n, 1)
  }  
}