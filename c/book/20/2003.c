#include <stdio.h>
#include <stdlib.h>

int main()
{
    int *arr;
    int x;

    arr = (int *)malloc(sizeof(int) * 3);
    if (arr == NULL)
    {
        puts("Unable to allocate memory");
        return(1);
    }

    for (x=0; x < 3; x++)
    {
        *(arr+x) = (x+1)*100;
        printf("Int %i is: %i\n", x+1, (arr[x]));
    }
    return(0);
}
