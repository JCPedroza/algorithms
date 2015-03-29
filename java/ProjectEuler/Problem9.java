/*
projecteuler.net problem 9.

Special Pythagorean triplet.

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which:

a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.

Find the product abc.
*/

public class Problem9 {


    // Helper for solution1. Checks if a triplet is pythagorean.
    public static boolean isPythTriplet(int a, int b, int c) {
        if (a*a + b*b == c*c || b*b + c*c == a*a || a*a + c*c == b*b) {
            if (a != b && b != c) {
                return true;
            }
        }
        return false;
    }

    // Helper for solution2. Checks if the input is a perfect square.
    public static boolean isPerfectSquare(int n) {
        int closestRoot = (int) Math.sqrt(n);
        return n == closestRoot * closestRoot;
    }

    // Brute force three for loop solution. Check if a + b + c == 1000 and
    // if a, b, c is a Pythagorean triplet. If so, return the product.
    public static int solution1() {
        for (int a = 1; a < 1000; a++) {
            for (int b = a + 1; b < 1000; b++) {
                for (int c = b + 1; c < 1000; c++) {
                    if (a + b + c == 1000) {
                        if (isPythTriplet(a, b, c)) {
                            return a * b * c;
                        }
                    }
                }
            }
        }
        return -1;
    }

    // Brute force two for loop solution. Checks if a^2 + b^2 is a perfect 
    // square, then if a + b + c == 1000.
    public static int solution2() {
        int sumOfSquares;
        for (int a = 1; a < 1000; a++) {
            for (int b = a + 1; b < 1000; b++) {
                sumOfSquares = a*a + b*b;
                if (isPerfectSquare(sumOfSquares)) {
                    if (a + b + Math.sqrt(sumOfSquares) == 1000) {
                        return a * b * ((int) Math.sqrt(sumOfSquares));
                    }
                }
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        System.out.println(solution1());
        System.out.println(solution2());
    } 
}