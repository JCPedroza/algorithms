/*
projecteuler.net problem 4.

Largest palindrome product.

A palindromic number reads the same both ways. The largest palindrome made 
from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
*/

public class Problem4 {

    // Checks if a number is a palindrome
    public static boolean isPalindrome(int n) {
        int reversed = 0;
        int number = n;

        while (number > 0) {
            reversed = 10 * reversed + (number % 10);
            number = number / 10;
        }
        
        return reversed == n;
    }

    // Finds the largest palindrome made from the product of two 3-digit numbers.
    public static int largestPalindromeProduct() {
        int product = 0;
        int largestPalindrome = 0;
        
        for (int a = 999; a >= 100; a--) {
            for (int b = 999; b >= a; b--) {
                product = a * b;
                if (product <= largestPalindrome) {
                    break;
                }
                if (isPalindrome(product)) {
                    largestPalindrome = product;
                }
            }
        }

        return largestPalindrome;
    }

    public static void main(String[] args) {
        System.out.println(largestPalindromeProduct());
    }

}