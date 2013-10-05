# Different implementations of a simple factorial algorithm.
# To run this script: source("factorial.R")

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
  acc <- 1
  while (n > 1){
    acc <- acc * n
    n   <- n - 1
  }
  acc
}

# Computes factorial of n using iteration and for loop.
factorialIterF <- function(n){
  acc <- 1
  for (i in n:1) acc = acc * i
  acc
}

# ===============================
#      Timing the Algorithms
# ===============================

repeats <- 5000

cat("\n")
cat("===========================================================================\n")
cat("\n")
cat("Running time of different factorial algorithm implementations, CPU time, in seconds.\n")
cat(sprintf("Compute 150 factorial %i times:\n", repeats))

cat("\n"); 
cat("factorialRecursive()\n")
print(system.time(replicate(repeats, factorialRecursive(150))))

cat("\n")
cat("factorialTailRecursive()\n")
print(system.time(replicate(repeats, factorialTailRecursive(150))))

cat("\n")
cat("factorialIterW()\n")
print(system.time(replicate(repeats, factorialIterW(150))))

cat("\n")
cat("factorialIterF()\n")
print(system.time(replicate(repeats, factorialIterF(150))))

cat("\n")
cat("===========================================================================\n")
cat("\n")
