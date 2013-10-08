/**
* Determines if a list of characters is balanced, recursively.
*
* What exactly does it mean for a string to be balanced?
* 
* A string with no parentheses in it is balanced. Any given opening parenthesis is balanced
* if and only if there's a closing parenthesis to the right of it such that the expression
* between them is also balanced. Any given closing parenthesis is balanced if and only if
* there's an opening parenthesis to the left of it such that the expression between them
* is also balanced. An expression is balanced if and only if all of the parentheses in it
* are balanced.
*
* Counting the number of '(' and ')' is not enough. This example ")s(" has an equal number of
* opening and closing parentheses, but it is not balanced. During the scan, you also need to make 
* sure that the number of opening parentheses is always greater or equal to the number of closing
* parentheses. 
*/
object BalancedParentheses{
  
  /** 
  * Determines if a list of characters is balanced, recursively.
  *
  * Implements a counter, every '(' counts as +1, every ')' counts as -1. This achieves
  * 2 things:
  * 1) Make sure that in the end there is an equal number of '(' and ')'.
  * 2) If the counter is negative in any iteration, it means that at that moment there
  * are more ')' than '(', which means that the string is not balanced.
  * 
  * The counter is not implemented as mutable data, as a variable. Instead, depending on
  * the case, the recursion is called with a modified parameter. 
  */
  def balance(chars: List[Char]): Boolean = {
    def balanceIter(chars: List[Char], count: Int): Boolean = 
      if      (chars.isEmpty)      count == 0 // end of the scan, is count == 0? is the string balanced?
      else if (count < 0)          false // number of '(' must be >= ')' through the scan
      else if (chars.head == '(')  balanceIter(chars.tail, count + 1) // '(' found, +1 to count
      else if (chars.head == ')')  balanceIter(chars.tail, count - 1) // ')' found, -1 to count
      else                         balanceIter(chars.tail, count) // no parentheses on this iteration
    balanceIter(chars, 0) 
  }
}