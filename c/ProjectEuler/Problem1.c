/* 
Multiples of 3 and 5
Problem 1

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
*/

#include <stdio.h>

int sum_multiples_of_3_or_5(int range) {

    int result = 0;

    for (int i = 1; i <= range; i++) {
        if (i % 3 == 0 || i % 5 == 0) {
            result += i;
        }
    }

    return result;

}

int main(int argv, char* argc[]) {

    printf("\n\nThe sum of the natural multiples of 3 or 5 bellow 1000 is: %d\n\n", 
            sum_multiples_of_3_or_5(999));

    return 0;
}