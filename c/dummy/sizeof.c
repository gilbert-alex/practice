#include <stdio.h>

int main()
{
    int *ip;
    printf("Size of int pointer:\t%lu\n", sizeof(ip));
    char *cp;
    printf("Size of char pointer:\t%lu\n", sizeof(cp));
    char *dp;
    printf("Size of double pointer:\t%lu\n", sizeof(dp));

    long *lp;
    printf("Size of long pointer:\t%lp\n", sizeof(lp));
    return 0;
}