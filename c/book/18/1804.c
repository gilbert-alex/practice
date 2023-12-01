#include <stdio.h>

int main()
{
    int arr[5];

    printf("The array has a size of %u.\n", sizeof(arr));

    for(int x=0; x<5; x++)
    {
        printf("This position of the array has a size of %u.\n", sizeof(arr[x]));
    }
    return(0);
}
