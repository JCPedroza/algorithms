fn main() {
    println!("{}", factorial_iterative(10));
    println!("{}", factorial_recursive(10));
    println!("{}", factorial_tail_recursive(10));
}

// Using iteration
fn factorial_iterative(n: int) -> int {
    let mut acc: int = 1;
    for i in range(1, n + 1) {
        acc *= i;
    }
    acc
}

// Using recursion
fn factorial_recursive(n: int) -> int {
    if n == 1 {
        return 1;
    }
    n * factorial_recursive(n - 1)
}

// Using tail recursion
fn factorial_tail_recursive(n: int) -> int {
    fn factorial_tail_helper(n: int, acc: int) -> int {
        if n == 1 {
            return acc;
        }
        factorial_tail_helper(n - 1, acc * n)
    }
    factorial_tail_helper(n, 1)
}







