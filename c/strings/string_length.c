// Algorithms to calcualte the length of a char*

#include <stdio.h>
#include <stdlib.h>
#include "../timeutils.h"

// =========================================================================
//                              Functions
// =========================================================================

/* Calculates the length of a char* using a while loop and char* index. */
int length_1(char* s) {
    int length = 0;
    while (s[length] != '\0') {
        length++;
    }
    return length;
}

/** Calculates the length of a char* using a while loop and pointer. */
int length_2(char* s) {
    const char *start = s;
    while (*s) {
        s++;
    }
    return s - start;
}

/* Calculates the length of a char*, FreeBSD algorithm: 
http://fxr.watson.org/fxr/source/libkern/strlen.c?v=DFBSD */
int length_3(char* str) {
    const char* s;
    for (s = str; *s; ++s);
    return(s - str);
}

/* Calculates the length of a char*, vectorized strlen algorithm:
http://www.strchr.com/optimized_strlen_function 
---> for x86 only <--- */
int length_4(char* s) {
    size_t len = 0;
    for(;;) {
        unsigned x = *(unsigned*)s;
        if((x & 0xFF) == 0) return len;
        if((x & 0xFF00) == 0) return len + 1;
        if((x & 0xFF0000) == 0) return len + 2;
        if((x & 0xFF000000) == 0) return len + 3;
        s += 4, len += 4;
    }
}

// =========================================================================
//                             main() & timing
// =========================================================================

int main(int argc, char* argv[]) {
    
    char* word  = "abcabcabcabcabcabcabcabacbacbacbacbcabcabcacabieiruewirwqeriuwerid\
                   ierouqwirwefsdfasfdsfdskfasjdfdsfajsfjdjasdjjdsajfdjdfadsfadffsfaf\
                   219123890218903890213890218391208938901238901208931028938091238912\
                   sdkljfklsdjfs90dfajdskf90sdfjkdsf098asfjkladsf09sdfjkladsf0adfsdfj\
                   dklfaklsdfjdksfjksdjfklsdjfklasjdfksdlfksadklfjksadlfjlaksfklsjdjf\
                   sdjkfisdds98fsd9f9asdf89s8df9ds8fds9f8sa98fasjfksnmfsndmfmnasdfmna\
                   adsfjkldkslfds90ds90dasjkldsfjkdsjksdjklafdsjklajkljljkalsjkldjkla\
                   kldjfkldsfjksdljfkdsfiodsufalsdfjkslafksfjsdkjfskflklsfjdsfjalskfj\
                   kldjfkldsfjksdljfkdsfiodsufalsdfjkslafksfjsdkjfskflklsfjdsfjalskfj\
                   kldjfkldsfjksdljfkdsfiodsufalsdfjkslafksfjsdkjfskflklsfjdsfjalskfj\
                   kldjfkldsfjksdljfkdsfiodsufalsdfjkslafksfjsdkjfskflklsfjdsfjalskfj\
                   kldjfkldsfjksdljfkdsfiodsufalsdfjkslafksfjsdkjfskflklsfjdsfjalskfj\
                   kldjfkldsfjksdljfkdsfiodsufalsdfjkslafksfjsdkjfskflklsfjdsfjalskfj\
                   df sdf afs 1 11 1 1 11 1  jf kasd ds0f s0fasd fa0sf a0 f0a fas0 fs\
                   kkkkkdfjdfsdifjsdafisdjfisdjfsidfjasidfahsdfiashdfiashfishfiashfih\
                   df sdf afs 1 11 1 1 11 1  jf kasd ds0f s0fasd fa0sf a0 f0a fas0 fs\
                   df sdf afs 1 11 1 1 11 1  jf kasd ds0f s0fasd fa0sf a0 f0a fas0 fs\
                   df sdf afs 1 11 1 1 11 1  jf kasd ds0f s0fasd fa0sf a0 f0a fas0 fs\
                   df sdf afs 1 11 1 1 11 1  jf kasd ds0f s0fasd fa0sf a0 f0a fas0 fs\
                   adfafafasfasdfasdfasdfasdfsfadsfsdf98912jds9dafbadfjadfjdasfdfadsf\
                   df sdf afs 1 11 1 1 11 1  jf kasd ds0f s0fasd fa0sf a0 f0a fas0 fs\
                   df sdf afs 1 11 1 1 11 1  jf kasd ds0f s0fasd fa0sf a0 f0a fas0 fs\
                   df sdf afs 1 11 1 1 11 1  jf kasd ds0f s0fasd fa0sf a0 f0a fas0 fs\
                   df sdf afs 1 11 1 1 11 1  jf kasd ds0f s0fasd fa0sf a0 f0a fas0 fs\
                   df sdf afs 1 11 1 1 11 1  jf kasd ds0f s0fasd fa0sf a0 f0a fas0 fs\
                   df sdf afs 1 11 1 1 11 1  jf kasd ds0f s0fasd fa0sf a0 f0a fas0 fs\
                   df sdf afs 1 11 1 1 11 1  jf kasd ds0f s0fasd fa0sf a0 f0a fas0 fs\
                   df sdf afs 1 11 1 1 11 1  jf kasd ds0f s0fasd fa0sf a0 f0a fas0 fs\
                   df sdf afs 1 11 1 1 11 1  jf kasd ds0f s0fasd fa0sf a0 f0a fas0 fs\
                   df sdf afs 1 11 1 1 11 1  jf kasd ds0f s0fasd fa0sf a0 f0a fas0 fs";

    long  times = 100000;

    // Check first that all algorithms are calculating the same length.
    int a = length_1(word);
    int b = length_2(word);
    int c = length_3(word);
    int d = length_4(word);
    if (a != b || a != c || a != d) {
        printf("\nInequality in algorithm results!!!\n\n");
        return 0;
    }

    double time_1 = time_it_char(word, times, length_1);
    double time_2 = time_it_char(word, times, length_2);
    double time_3 = time_it_char(word, times, length_3);
    double time_4 = time_it_char(word, times, length_4);

    double average_1 = time_1 / times;
    double average_2 = time_2 / times;
    double average_3 = time_3 / times;
    double average_4 = time_4 / times;

    printf("\n");
    printf("==============================================\n");
    printf("==============================================\n\n");
    printf("Char* Length Algorithm\n");
    printf("Char* length: %d\n", length_1(word));
    printf("Repetitions: %ld\n", times);
    printf("(all results are in seconds) \n");
    printf("----------------------------------------------\n");
    printf("\n");

    printf("Total time:\n");
    printf("1:  %f\n", time_1);
    printf("2:  %f\n", time_2);
    printf("3:  %f\n", time_3);
    printf("4:  %f\n", time_4);

    printf("\n");

    printf("Average time:\n");
    printf("1:  %f\n", average_1);
    printf("2:  %f\n", average_2);
    printf("3:  %f\n", average_3);
    printf("4:  %f\n", average_4);

    printf("\n");
    printf("==============================================\n");
    printf("==============================================\n\n");

    return 0;

}