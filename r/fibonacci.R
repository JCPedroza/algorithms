# =================================
#          The Algorithms
# =================================


# Calculates the nth fibonacci number, recusrively, without tail recursion.
# Performance: O(2^n).
fiboRecursive <- function(n) {
  if (n < 2) n
  else fiboRecursive(n - 1) + fiboRecursive(n - 2)
}