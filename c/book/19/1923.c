#include <stdio.h>

void swap(int *a, int *b);

int main()
{
    int a = 300;
    int b = 200;

    printf("Before swap: a=%i and b=%i\n", a, b);

    swap(&a, &b);

    printf("After swap: a=%i and b=%i\n", a, b);
    return(0);
}

void swap(int *a, int *b)
{
    int temp;
    if (*a > *b)
    {
        temp = *a;
        *a = *b;
        *b = temp;
    }
}
