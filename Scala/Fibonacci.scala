/**
* Different algorithms to calculate the nth fibonacci number. 
*/
object Fibonacci extends App{
  
  // =================================
  //          The Algorithms
  // =================================

  /**
  * Calculates the nth fibonacci number, recusrively, without tail recursion.
  * Performance: O(2^n).
  */
  def fiboRecursive(n: Int): Int = {
    if      (n == 0) 0
    else if (n == 1) 1
    else    fibo(n-1) + fibo(n-2)
  }
  
  /**
  * Calculates the nth fibonacci number, using tail recursion. 
  */
  def fiboTailRecursive(n: Int): Int = {
    def recursion(n: Int, a: Int, b: Int): Int = {
      if (n > 0) recursion(n - 1, b, a + b)
      else       a
    }
    recursion(n, 0, 1)
  }

  /**
  * Calculates the nth fibonacci number, using iteration.
  */
  def fiboIter(n: Int): Int = {
    var a = 0
    var b = 1
    for (i <- 0 to n){
      var buffer = a
      a = b
      b = buffer + b
    }
    a
  }
  
  /** 
  * Calculates the nth fibonacci number, using Binet's formula
  */
  def fiboBinet(n: Int): Int =
    ((pow(1 + sqrt(5), n) - (pow(1-sqrt(5), n))) / (pow(2, n) * sqrt(5))).asInstanceOf[Int]
  
  /** 
  * Calculates the nth fibonacci number, based on these formulas:
  * F(2n-1) = F(n)^2 + F(n-1)^2
  * F(2n) = (2F(n-1) + F(n))*F(n)
  */
  def fib(n:Int):BigInt = {
    def fibs(n:Int):(BigInt,BigInt) = if (n == 1) (1,0) else {
      val (a,b) = fibs(n/2)
      val p = (2*b+a)*a
      val q = a*a + b*b
      if(n % 2 == 0) (p,q) else (p+q,p)
    }
    fibs(n)._1
  }
  
  /**
  * Calculates the nth fibonacci number, using lazy sequence (also known as stream).
  */
  def fiboLazy: Stream[Int] = 0 #:: 1 #:: fiboLazy.zip(fiboLazy.tail).map{case (a,b) => a + b}

  // =================================
  //                Tests
  // =================================

}