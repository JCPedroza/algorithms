/*
projecteuler.net problem 16.

Power digit sum.

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 2^1000?
*/

import java.math.BigInteger;

public class Problem16 {

    private static final int EXPONENT = 1000;

    private BigInteger solution() {
        BigInteger theNumber = new BigInteger("2").pow(EXPONENT);
        BigInteger theSum = BigInteger.ZERO;

        while (theNumber.compareTo(BigInteger.ZERO) > 0) {
            BigInteger[] results = theNumber.divideAndRemainder(BigInteger.TEN);
            theSum = theSum.add(results[1]);
            theNumber = results[0];
        }

        return theSum;
    }

    /** Print result. */
    public static void main(String[] args) {
        System.out.println(new Problem16().solution());
    }
}