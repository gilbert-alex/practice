#include <stdio.h>

int main()
{
    int age;
    float weight;

    int *a = &age;
    float *w = &weight;

    *a = 35;
    *w = 200.1;

    printf("My age is %i and weight is %.1f\n", age, weight);
    return(0);
}
