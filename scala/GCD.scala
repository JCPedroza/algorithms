object GCD{

  /** Computes the greatest common divisor of two numbers using Euclid's algorithm */
  def gcd(a: Int, b: Int): Int = 
    if (b == 0) a else gcd(b, a % b)

}
