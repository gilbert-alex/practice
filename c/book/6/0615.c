#include <stdio.h>

int main ()
{
    const int v = 10;

    printf("The value is %d\n", v);
    printf("And %d is the value\n", v);
    printf("It's not %d\n", v+1);
    printf("And it's not %d\n", v-1);
    printf("No, the values is %d\n", v);
    return(0);
}
