/*
projecteuler.net problem 5.

Smallest multiple.

2520 is the smallest number that can be divided by each of the numbers 
from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of 
the numbers from 1 to 20?
*/

public class Problem5 {

    // Simple while loop. Numbers in strides of 20 are tested until
    // one divisible by all the numbers in the range is found.
    public static long solution1() {
        int stride = 20;
        int current = 20;
        int sum = 0;

        while (true) {
            sum = 0;
            for (int n = 2; n <= 20; n++) {
                sum += current % n;
            }
            if (sum == 0) {
                return current;
            }
            current += stride;
        }
    }

    
    public static void main(String[] args) {
        System.out.println(solution1());
    }
}