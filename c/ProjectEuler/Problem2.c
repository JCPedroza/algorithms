/*
Even Fibonacci numbers

Problem 2

Each new term in the Fibonacci sequence is generated by adding the previous two terms. 
By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, 
find the sum of the even-valued terms.
*/

#include <stdio.h>

// First implementation.
long even_fibonacci_sum(long limit) {

    long sum     = 0;
    long current = 1; 
    long last    = 0; 
    long buffer;

    while (current < limit) {

        if (current % 2 == 0) {
            sum += current;
        }

        buffer  = current;
        current = current + last;
        last    = buffer;
        
    }

    return sum;
}

// We can get rid of the testing for even values. Every third Fibonacci number is even.
// Change the program so that only every third number is added.
long better_even_fibonacci_sum(long limit) {

    long sum    = 0;
    long first  = 1;
    long second = 1;
    long third  = first + second;

    while (third < limit) {
        sum += third;
        first  = second + third;
        second = third  + first;
        third  = first  + second;
    }

    return sum;

}

int main(int argc, char* argv[]) {

    printf("\n%ld\n\n", even_fibonacci_sum(4000000));
    printf("\n%ld\n\n", better_even_fibonacci_sum(4000000));

    return 0;
} 