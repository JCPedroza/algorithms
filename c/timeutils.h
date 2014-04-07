#ifndef TIMEUTILS_H_INCLUDED
#define TIMEUTILS_H_INCLUDED

double time_it(long n, long times, long(*f)(long)); 

double time_it_char(char* s, long times, int(*f)(char*));

#endif

