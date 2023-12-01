#include <stdio.h>
#include <time.h>

int main()
{
    time_t tictok;

    time(&tictok);
    printf("The time is now %ld\n",tictok);
    return(0);
}
