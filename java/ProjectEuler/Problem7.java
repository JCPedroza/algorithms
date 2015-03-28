/*
projecteuler.net problem 7.

10001st prime.

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we 
can see that the 6th prime is 13.

What is the 10,001st prime number?
*/

public class Problem7 {

    // Loop through numbers and use trial division for primarly test, keep
    // count of which ones are prime, return the nth prime.
    public static int nthPrime(int n) {
        int count = 0;
        int current = 1;
        while (count < n) {
            current++;
            if (Helpers.isPrimeTrialDivision(current)) {
                count++;
            }
        }
        return current;
    }

    public static void main(String[] args) {
        System.out.println(nthPrime(10001));
    }
}