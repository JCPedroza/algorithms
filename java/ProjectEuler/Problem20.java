/*
projecteuler.net problem 20.

Factorial digit sum.

n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
*/

import java.math.BigInteger;

public class Problem20 {

    public static final BigInteger TEN = BigInteger.TEN;
    public static final BigInteger ONE = BigInteger.ONE;
    public static final BigInteger ZERO = BigInteger.ZERO;
    public static final BigInteger THE_NUMBER = new BigInteger("100");

    /** Computes the factorial of a BigInteger. */
    public static BigInteger bigFactorial(BigInteger n) {
        BigInteger total = ONE;
        for (BigInteger i = n; i.compareTo(ONE) > 0; i = i.subtract(ONE)) {
            total = total.multiply(i);
        }
        return total;
    }

    /** Computes the sum of the digits of a BigInteger. */
    public static BigInteger digitSum(BigInteger n) {
        BigInteger sum = ZERO;
        while (n.compareTo(ZERO) > 0) {
            BigInteger[] divAndRem = n.divideAndRemainder(TEN);
            BigInteger digit = divAndRem[1];
            sum = sum.add(digit);
            n = divAndRem[0];
        }
        return sum;
    }

    /** Finds the sum of the digits in the given factorial. */
    public static BigInteger solution(BigInteger n) {
        return digitSum(bigFactorial(n));
    }

    /** Print solution. */
    public static void main(String[] args) {
        System.out.println(solution(THE_NUMBER));
    }
}