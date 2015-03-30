/*
Different implementations of the Sieve of Eratosthenes algorithm.

http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
*/

// TODO: check if LinkedList is faster than ArrayList for very big limit.

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Arrays;

public class SieveOfEratosthenes {

    /**
     * A naive implementation that can be improved upon. We know 2 is the only even
     * prime number, so there's no need to include them in the algorithm, wastes space
     * and time.
     */
    public static ArrayList<Integer> getPrimes1(int limit) {
        int crossLimit = (int) Math.sqrt(limit);
        boolean[] sieve = new boolean[limit+1];
        ArrayList<Integer> primes = new ArrayList<Integer>(Arrays.asList(2));

        for (int n = 4; n <= limit; n += 2) {   // mark even mumbers > 2
            sieve[n] = true;
        }

        for (int n = 3; n <= crossLimit; n += 2) { 
            if (!sieve[n]) {   // n not marked, hence prime
                for (int m = n*n; m <= limit; m += 2*n) {
                    sieve[m] = true;
                }
            }
        }

        for (int i = 3; i <= limit; i += 2) {
            if (!sieve[i]) {
                primes.add(i);
            }
        }

        return primes;
    }

    /**
     * Optimized to don't use even numbers.
     */
    public static ArrayList<Integer> getPrimes2(int limit) {
        int sieveBound = (limit - 1) / 2;    // last index of sieve
        boolean[] sieve = new boolean[sieveBound];
        double crossLimit = (Math.floor(Math.sqrt(limit)) - 1) / 2;
        ArrayList<Integer> primes = new ArrayList<Integer>(Arrays.asList(2));

        for (int i = 1; i < crossLimit; i++) {
            if (!sieve[i]) {
                int stepSize = 2 * i + 1;
                for (int j = 2*i*(i+1); j < sieveBound; j += stepSize) {
                    sieve[j] = true;
                }
            }
        }

        for (int i = 1; i < sieveBound; i++) {
            if (!sieve[i]) {
                primes.add(2*i+1);
            }
        }

        return primes;
    }

    public static void main(String[] args) {

        int repeats = 10;
        int lowerLimit = 10000;
        int limit = 20000;
        int stride = 5;
        double multiplier = 1.0 / repeats;
        int nresults = (limit - lowerLimit) / stride;
        double[][] results1 = new double[nresults][2];
        double[][] results2 = new double[nresults][2];

        // getPrimes1
        for (int n = lowerLimit, i = 0; n < limit; n += stride, i++) {
            long startTime = System.nanoTime();
            getPrimes1(i);
            double totalTime = (System.nanoTime() - startTime) * multiplier;
            results1[i] = new double[]{n, totalTime};
        }

        // getPrimes2
        for (int n = lowerLimit, i = 0; n < limit; n += stride, i++) {
            long startTime = System.nanoTime();
            getPrimes2(i);
            double totalTime = (System.nanoTime() - startTime) * multiplier;
            results2[i] = new double[]{n, totalTime};
        }

        for (double[] r : results2) {
            System.out.println(String.format("%f %f", r[0], r[1]));
        }

    }
}