/*
projecteuler.net problem 14

Longest Collatz sequence

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 
10 terms. Although it has not been proved yet (Collatz Problem), it is thought that 
all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
*/

public class Problem14 {

    public static final int LIMIT = 1000000;

    public static boolean isEven(long n) {
        return n % 2 == 0;
    }

    public static long even(long n) {
        return n / 2;
    }

    public static long odd(long n) {
        return 3 * n + 1;
    }

    public static long solution(long limit) {
        long maxNum = 1;
        long maxSequence = 1;

        for (long n = 1; n < limit; n++) {
            long result = n;
            long sequence = 1;

            while (result != 1) {
                if (isEven(result)) {
                    result = even(result);
                } else {
                    result = odd(result);
                }
                sequence++;
            }

            if (sequence > maxSequence) {
                maxSequence = sequence;
                maxNum = n;
            }
        }

        return maxNum;
    }

    public static void main(String[] args) {
        System.out.println(solution(LIMIT));
    }
}