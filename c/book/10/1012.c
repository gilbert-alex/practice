#include <stdio.h>

void limit(int stop);

int main()
{
    int s;

    printf("Enter a stopping value (0-100): ");
    scanf("%d",&s);
    limit(s);
    return(0);
}

void limit(int stop)
{
    for(int x = 0; x <= 100; x++)
    {
        printf("%d ",x);
        if(x == stop)
        {
            puts("You won!");
            return;
        }
    }
    puts("I won!");
}
