# ===============================
#        The Algorithms
# ===============================

# Computes factorial of n using recursion.
factorialRecursive <- function(n){
  if (n == 1) 1
  else n * (factorial(n - 1))
}

# Computes factorial of n using tail recursion.
factorialTailRecursive <- function(n){
  recursion <- function(n, acc){
    if (n < 1) acc
    else recursion(n-1, acc * n)
  }
  recursion(n, 1)
}

# Computes factorial of n using iteration and while loop.
factorialIterW <- function(n){
  acc = 1
  while (n > 1){
    acc = acc * n
    n   = n - 1
  }
  acc
}

# Computes factorial of n using iteration and for loop.
factorialIterF <- function(n){
  acc = 1
  for (i in n:1) acc = acc * i
  acc
}