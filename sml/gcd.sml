(* Computes the greatest common divisor of two numbers using Euclid's algorithm *)
fun gcd(a : int, b : int): int = 
    if   b = 0
    then a
    else gcd(b, a mod b)





