#include <stdio.h>
#include <math.h>

int main()
{
    int values[] = {10, 12, 14, 15, 16, 18, 20};

    int counter = 0;
    while(values[counter]>0)
    {
        counter ++;
    }

    float square[counter];

    for(int x = 0; x < counter; x++)
    {
        square[x] = sqrt(values[x]);
        printf("The square root of %d is %.2f.\n", values[x], square[x]);
    }
    return(0);
}
