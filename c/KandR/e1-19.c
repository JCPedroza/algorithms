#include <stdio.h>

char* reverse(char s[]);
int   strsize(char s[]);

// Exercise 1-19. Write a function reverse(s) that reverses the character string s. 
// Use it to write a program that reverses its input a line at a time.
int main() {
    return 0;
}

// Returns a reversed copy of the input string // TODO
const char* reverse(char s[]) {
    int   length = strsize(s);
    int   i, j;
    char  reversed[length + 1];
     
    for (j = 0, i = length - 1; i > 0; j++, i--) {
        reversed[j] = s[i];
    }
    reversed[length] = '\0';

    return reversed;
}

// Returns the length of a string
int strsize(char* s) {
    size_t len = 0;
    for (;;) {
        unsigned x = *(unsigned*)s;
        if ((x & 0xFF) == 0)       return len;
        if ((x & 0xFF00) == 0)     return len + 1;
        if ((x & 0xFF0000) == 0)   return len + 2;
        if ((x & 0xFF000000) == 0) return len + 3;
        s += 4, len += 4;
    }
}



