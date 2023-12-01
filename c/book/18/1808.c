#include <stdio.h>

int main()
{
    int arr[] = { 100, 200, 300, 400, 500};

    for(int x = 0; x < 5; x++)
    {
        printf("value at array %d is %d held at address %lu\n", x+1, arr[x], &arr[x]);
    }
    return(0);
}
