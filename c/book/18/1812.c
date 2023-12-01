#include <stdio.h>

int main()
{
    int a = 100;
    int *p = &a;

    printf("Value: %i\n", *p);
    printf("Value: %i\n", a);
    printf("Address of 'a': %p\n", p);
    printf("Address of 'p': %p\n", &p);
    return(0);
}
