/*
projecteuler.net problem 3.

Largest prime factor.

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
*/

import java.lang.Math;

public class Problem3 {

    public static final long NUMBER = 600851475143L;
    
    public static long largestPrimeFactor(long n) {

        long lastFactor, factor, maxFactor;

        if (n % 2 == 0) {
            lastFactor = 2;
            n = n / 2;
            while (n % 2 == 0) {
                n = n / 2;
            }
        } else {
            lastFactor = 1;
        }

        factor = 3;
        maxFactor = (long) Math.ceil(Math.sqrt(n));  // every number n can at most have one prime factor greater than sqrt(n)
 
        while (n > 1 && factor <= maxFactor) {
            if (n % factor == 0) {
                n = n / factor;
                lastFactor = factor;
                while (n % factor == 0) {
                    n = n / factor;
                }
                maxFactor = (long) Math.ceil(Math.sqrt(n));
            }
            factor = factor + 2; // 2 is the only even prime, so if we treat 2 separately 
        }                        // we can increase factor with 2 every step.
        
        if (n == 1) {
            return lastFactor;
        } else {
            return n;
        }


    }

    public static void main(String[] args) {
        System.out.println(largestPrimeFactor(NUMBER));
    }
}