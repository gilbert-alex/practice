#include <stdio.h>

int main()
{
    float marketclose[] = {24164.95, 24107.08, 24643.63, 24400.93, 23728.53};

    int counter = 0;
    while(marketclose[counter]>0)
    {
            counter += 1;
    }

    puts("Stock Market Close");
    for(int x = 0; x < counter; x++)
    {
        printf("Day %d: %.2f\n", x+1, marketclose[x]);
    }
    return (0);
}
