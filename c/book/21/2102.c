#include <stdio.h>
#include <time.h>

int main()
{
    time_t tictok;

    tictok = time(NULL);
    printf("The time is now %ld\n", tictok);
    return(0);
