#ifndef TIMEUTILS_H_INCLUDED
#define TIMEUTILS_H_INCLUDED

/* Measures the CPU time of a function executed x times */
double time_it(long n, long times, long(*f)(long)); 

#endif

