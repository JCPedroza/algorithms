# =================================
#          The Algorithms
# =================================


# Calculates the nth fibonacci number, recusrively, without tail recursion.
# Performance: O(2^n).
fiboRecursive <- function(n){
  if      (n == 0) 0
  else if (n == 1) 1
  else fiboRecursive(n - 1) + fiboRecursive(n - 2)
}