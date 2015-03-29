/*
projecteuler.net problem 10.

Summation of primes.

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
*/

import java.util.ArrayList;

public class Problem10 {

    public static final int LIMIT = 2000000;

    // Loop through all odd numbers up to the limit, primarly check using
    // trial division, add n if prime.
    public static long sumOfPrimes1(int limit) {
        long sum = 5;  // 2 and 3 are prime
        for (int n = 5; n < limit; n += 2) {
            if (Helpers.isPrimeTrialDivision(n)) {
                sum += n;
            }
        }
        return sum;
    }

    public static long sumOfPrimes2(int limit) {
        ArrayList<Integer> primes = Helpers.sieveOfEra(limit);
        long sum = 0;
        for (int n : primes) {
            sum += n;
        }
        return sum;
    }

    public static void main(String[] args) {
        System.out.println(sumOfPrimes1(LIMIT));
        System.out.println(sumOfPrimes2(LIMIT));
    }
}