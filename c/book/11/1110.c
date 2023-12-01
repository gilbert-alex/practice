#include <stdio.h>

int main()
{
    int x;

    x = 5;

    while(x <= 100)
    {
        printf("%d, ", x);
        x+=5;
    }
    putchar('\n');

    for(int cinq = 5; cinq < 101; cinq+=5)
    {
        printf("%d ", cinq);
    }
    putchar('\n');
    return(0);
}
