object Factorial{

  /** Computes factorial of n. */
  def factorial(n: Int): Int = 
    if (n == 0) 1 else n * factorial(n - 1)

}