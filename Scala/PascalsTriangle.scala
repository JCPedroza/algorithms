/**
* Pascal's Triangle operations.
*
* The following pattern of numbers is called Pascal’s triangle:
*
*     1
*    1 1
*   1 2 1
*  1 3 3 1
* 1 4 6 4 1
*    ...
*
* Columns and rows representation:
* 
*    c0 c1 c2 c3 c4
* r0 1
* r1 1  1
* r2 1  2  1
* r3 1  3  3  1
* r4 1  4  6  4  1
* ...
*
* The numbers at the edge of the triangle are all 1, and each number inside the triangle 
* is the sum of the two numbers above it. 
*
* Pascal's rule (used to compute elements of the triangle):
*
* r   r - 1   r - 1
*   =       +
* c   c - 1     c
*
*/
object PascalsTriangle{
  
  /** 
  * Computes the elements of Pascal’s triangle, recursively, using Pascal's rule.
  * @param c Column.
  * @param r Row.
  */
  def pascal(c: Int, r: Int): Int = 
    if (c == 0 || c == r) 1                      // base case: edges are always 1
    else pascal(c - 1, r - 1) + pascal(c, r - 1) // apply pascal's rule recursively
  
  /**
  * Prints a pascal triangle of r rows.
  */
  def printPT(r: Int) {
    println("Pascal's Triangle")
    for (row <- 0 to r) {
      for (col <- 0 to row)
        print(pascal(col, row) + " ")
      println()
    }
  }
  
}