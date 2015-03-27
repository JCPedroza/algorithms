/*
Sum square difference.

The sum of the squares of the first ten natural numbers is:
1^2 + 2^2 + ... + 10^2 = 385.

The square of the sum of the first ten natural numbers is:
(1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten 
natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one 
hundred natural numbers and the square of the sum.
*/

public class Problem6 {

    public static int LIMIT = 100;

    // Loop, multiply, difference. No one likes equations.
    public static long solution1(long limit) {
        long sumOfSquares = 0;
        long squareOfSum = 0;

        for (int i = 1; i <= limit; i++) {
            sumOfSquares += i * i;
            squareOfSum += i;
        }
        squareOfSum *= squareOfSum;

        return squareOfSum - sumOfSquares;
    }

    // Better solution using aritmetic sum formulas.
    // 0 + 1 + 2 + ... + n = 1/2(n + 1)n
    // 0^2 + 1^2 + ... + n^2 = ((2n + 1)(n + 1)n) / 6
    public static long solution2(long limit) {
        long sum = ((limit + 1) * limit) / 2;
        long squareOfSum = sum * sum;
        long sumOfSquares = ((2 * limit + 1) * (limit + 1) * limit) / 6;
        return squareOfSum - sumOfSquares;

    }
    
    public static void main(String[] args) {
        System.out.println(solution1(LIMIT));
        System.out.println(solution2(LIMIT));
    }
}