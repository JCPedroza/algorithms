/*
projecteuler.net problem 21.

Amivable numbers.

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide 
evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a 
and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; 
therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
*/

import java.util.ArrayList;

public class Problem21 {

    /** Generates a list of proper divisors of n. */
    private ArrayList<Integer> getDivisors(int n) {
        ArrayList<Integer> list = new ArrayList<Integer>();
        int limit = (int) Math.sqrt(n);
        list.add(1);
        
        for (int i = 2; i <= limit; i++) {
            if (n % i == 0) {
                list.add(i);
                list.add(n / i);
            }
        }

        return list;
    }

    /** Returns the sum of the integers in a list. */
    private int listSum(ArrayList<Integer> list) {
        int sum = 0;
        for (int n : list) {
            sum += n;
        }
        return sum;
    }

    /**  Returns the sum of the proper divisors of n. */
    private int sumOfDivisors(int n) {
        return listSum(getDivisors(n));
    }

    /** Are a and b amicable? */
    private boolean areAmicable(int a, int b) {
        if (a == b) {
            return false;
        }
        return sumOfDivisors(a) == b && sumOfDivisors(b) == a;
    }

    private int solution(int limit) {
        ArrayList<Integer> list = new ArrayList<Integer>();
        for (int i = 1; i <= limit; i++) {
            for (int j = i + 1; j <= limit; j++) {
                if (areAmicable(i, j)) {
                    list.add(i);
                    list.add(j);
                }
            }
        }
        return listSum(list);
    }

    /** Print solution. */
    public static void main(String[] args) {
        System.out.println(new Problem21().solution(10000));
    }   
}