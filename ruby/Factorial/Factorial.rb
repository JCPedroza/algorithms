
# While loop
def factorial_w(n)
    validate(n)
    total = 1
    while n > 1
        total *= n
        n -= 1
    end
    total
end


# For loop
def factorial_f(n)
    validate(n)
    total = 1
    for i in (2 .. n)
        total *= i
    end
    total
end


# Recursive
def factorial_r_recursion(n)
    if n < 2
        1
    else
        n * factorial_r_recursion(n - 1)
    end
end

def factorial_r(n)
    validate(n)
    factorial_r_recursion(n)
end


# Tail-recursive
def factorial_tr_recursion(n, acc)
    if n < 2
        acc
    else
        factorial_tr_recursion(n - 1, n * acc)
    end
end

def factorial_tr(n, acc = 1)
    validate(n)
    factorial_tr_recursion(n, acc)
end


# Iterative with Range.each
def factorial_re(n)
    validate(n)
    if n == 0
        1
    else 
        (2 .. n - 1).each {|i| n *= i}
        n
    end
end


# Iterative with Range.inject
def factorial_ri(n)
    validate(n)
    (1 .. n).inject(:*) || 1 # || 1 handles n = 0 so !0 = 1
end


# Iterative with Range.reduce
def factorial_rr(n)
    validate(n)
    (1 .. n).reduce(:*) || 1 # || 1 handles n = 0 so !0 = 1
end


# Stirling's Approximation, will return infinity if n > 170
def factorial_sa(n)
    validate(n)
    Math.sqrt(2 * Math::PI * n) * (n / Math::E) ** n
end


# Helper for argument validation
def validate(n)
    if n < 0 or not n.kind_of? Integer
        raise ArgumentError, "n must be an integer and >= 0"
    end
end 

