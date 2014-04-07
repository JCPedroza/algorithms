// Algorithms to calcualte the length of a char*

#include <stdio.h>
#include <stdlib.h>
#include "../timeutils.h"

// =========================================================================
//                              Functions
// =========================================================================

/* Calculates the length of a char* using a while loop. */
int length_while(char* s) {
    int length = 0;
    while (s[length] != '\0') {
        length++;
    }
    return length;
}

/* Calculates the length of a char*, FreeBSD algorithm: 
http://fxr.watson.org/fxr/source/libkern/strlen.c?v=DFBSD */
int length_FBSD(char* str) {
    const char* s;
    for (s = str; *s; ++s);
    return(s - str);
}

// =========================================================================
//                             main() & timing
// =========================================================================

int main(int argc, char* argv[]) {
    
    if (argc != 3) {
        printf("\nusage: ./chars_length <chars> <repetitions>\n\n");
        return 1;
    }

    char* word  = argv[1];
    long  times = atol(argv[2]);

    double while_time = time_it_char(word, times, length_while);
    double FBSD_time  = time_it_char(word, times, length_FBSD);

    double while_average = while_time / times;
    double FBSD_average  = while_time / times;

    printf("\n");
    printf("==============================================\n");
    printf("==============================================\n\n");
    printf("Char* Length Algorithm\n");
    printf("Word: %s\n", word);
    printf("Repetitions: %ld\n", times);
    printf("(all results are in seconds) \n");
    printf("----------------------------------------------\n");
    printf("\n");

    printf("Total time:\n");
    printf("while loop:      %f\n", while_time);
    printf("FBSD algorithm:  %f\n", FBSD_time);

    printf("\n");

    printf("Average time:\n");
    printf("while loop:      %f\n", while_average);
    printf("FBSD algorithm:  %f\n", FBSD_average);

    printf("\n");
    printf("==============================================\n");
    printf("==============================================\n\n");

    return 0;

}