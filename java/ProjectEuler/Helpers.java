import java.util.ArrayList;
import java.util.Arrays;
import java.math.BigInteger;

public class Helpers {

    /** Primarly test using trial divison. */
    public static boolean isPrimeTrialDivision(int n) {
        if (n < 2) {
            return false;
        }
        if (n < 4) {
            return true;
        }
        if (n % 2 == 0 || n % 3 == 0) {
            return false;
        }

        int limit = (int) Math.sqrt(n);
        int divisor = 5;

        while (divisor <= limit) {
            if (n % divisor == 0 || n % (divisor + 2) == 0) {
                return false;
            }
            divisor += 6;
        }

        return true;
    }

    /** Returns the primes up to n using the Sieve of Eratosthenes. */
    public static ArrayList<Integer> sieveOfEra(int limit) {
        int crosslimit = (int) Math.sqrt(limit);
        boolean[] sieve = new boolean[limit+1];
        ArrayList<Integer> primes = new ArrayList<Integer>(Arrays.asList(2));

        for (int n = 4; n <= limit; n += 2) {   // mark even mumbers > 2
            sieve[n] = true;
        }

        for (int n = 3; n <= crosslimit; n += 2) { 
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

    /** Returns the number of digits in a BigInteger */
    public static int digits(BigInteger n) {
        int count = 0;
        while (n.compareTo(BigInteger.ZERO) > 0) {
            n = n.divide(BigInteger.TEN);
            count++;
        }
        return count;
    }

    public static void main(String[] args) {
        ArrayList<Integer> result = sieveOfEra(100);

        for (int n : result) {
            System.out.println(n);
        }

    }
}