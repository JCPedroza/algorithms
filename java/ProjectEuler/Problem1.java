/*
projecteuler.net problem 1.

Multiples of 3 and 5.

If we list all the natural numbers below 10 that are multiples of 3 or 5, 
we get 3, 5, 6 and 9. The sum of these multiples is 23. Find the sum of
all the multiples of 3 or 5 below 1000.
*/

public class Problem1{

    public static final int LIMIT = 1000;

    // Is n multiple of 5 or 3?
    public static boolean isMultiple(int n) {
        return n % 3 == 0 || n % 5 == 0;
    }
    
    // Returns the sum of all numbers bellow 1000 that are multiples of 3 or 5.
    public static int solution() {
        int total = 0;
        for (int i = 0; i < LIMIT; i++) {
            if (isMultiple(i)) {
                total += i;
            }
        }
        return total;
    }

    // Print solution
    public static void main(String[] args) {
        System.out.println(Problem1.solution());
    }

}