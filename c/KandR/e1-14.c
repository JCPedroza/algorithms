#include <stdio.h>
#include <limits.h>

#define NUM_CHARS CHAR_MAX

// Write a program to print a histogram of the frequencies of different characters in its input.
int main() {

    int i, c;
    int characters[NUM_CHARS] = {0};

    while ((c = getchar()) != EOF) {
            characters[c]++;
    }

    for (i = 0; i < NUM_CHARS; i++) {
        if (characters[i] > 0) {
            printf("%c: %d\n", i, characters[i]);
        }
    }

    return 0;
}