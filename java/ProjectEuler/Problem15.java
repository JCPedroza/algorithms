/*
projecteuler.net problem 15.

Lattice paths.

Starting in the top left corner of a 2×2 grid, and only being able to move to the 
right and down, there are exactly 6 routes to the bottom right corner.

(see image at https://projecteuler.net/problem=15)

How many such routes are there through a 20×20 grid?

TODO: everything, this doesn't WORK!
*/

import java.util.ArrayList;
import java.util.Arrays;

public class Problem15 {

    /** Compute n! */
    private double factorial(double n) {
        double fact = 1;
        for (double i = 1; i <= n; i++) {
            fact *= i;
        }
        return fact;
    }

    /**
     * Number of paths = the central binomial coefficients
     * (2n)! / (n!^2)
     */
    private double solution() {
        return factorial(2*20) / Math.pow(factorial(20), 2);
    }

    /** Print solution. */
    public static void main(String[] args) {
        System.out.printf("%.9f", new Problem15().solution());
        System.out.println();
    }
}