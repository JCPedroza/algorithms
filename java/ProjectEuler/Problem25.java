/*
projecteuler.net problem 25.

1000-digit Fibonacci number.

What is the first term in the Fibonacci sequence to contain 1000 digits?
1 = 1, 2 = 1, 3 = 2, 4 = 3, 5 = 5, 6 = 8, 7 = 13
*/

import java.math.BigInteger;

public class Problem25 {

    public static final int DIGITS = 1000;
    
    /** Counts the number of digits of an integer */
    public static int digits(BigInteger n) {
        int count = 0;
        while (n.compareTo(BigInteger.ZERO) > 0) {
            n = n.divide(BigInteger.TEN);
            count++;
        }
        return count;
    }

    /** Generator of fibonacci sequence */
    public static class Fibonacci {
        private BigInteger a, b, count, buffer;

        public Fibonacci() {
            a = BigInteger.ZERO;
            b = BigInteger.ONE;
            count = BigInteger.ZERO;
        }

        /** get the next Fibonacci number */
        public void next() {
            buffer = a; 
            a = a.add(b);
            b = buffer;
            count = count.add(BigInteger.ONE);
        }

        public BigInteger getCount() {
            return count;
        }

        public BigInteger getCurrent() {
            return a;
        }
    }

    public static BigInteger solution() {
        Fibonacci sequence = new Fibonacci();
        while (digits(sequence.getCurrent()) < DIGITS) {
            sequence.next();
        }
        return sequence.getCount();
    }
    
    /** Print solution */
    public static void main(String[] args) {
        System.out.println(solution());
    }
}

