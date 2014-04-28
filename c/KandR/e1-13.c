#include <stdio.h>

#define IN  1
#define OUT 0
#define MAXSIZE 10

// Write a program to print a histogram of the lengths of words in its input.
int main() {

    int i, j, c, state, lettercount;
    int wordcount[MAXSIZE] = {0};

    state = OUT;

    while ((c = getchar()) != EOF) {
        if (c == ' ' || c == '\n' || c == '\t') {
            state = OUT;
            wordcount[lettercount - 1]++;
            lettercount = 0;
        } else {
            state = IN;
            lettercount++;
        }
    }

    for (i = 0; i < MAXSIZE; i++) {
        printf("|%2d| ", i + 1);
        for (j = 1; j <= wordcount[i]; j++) {
            putchar('*');
        }
        putchar('\n');
    }

    return 0;

}
