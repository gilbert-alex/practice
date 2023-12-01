#include <stdio.h>

#define TRUE 1
#define FALSE 0

void limit(int count);
int verify (int check);

int main()
{
    int s;

    printf("Enter a stopping value (0-100): ");
    scanf("%d",&s);

    if(verify(s))
    {
        limit(s);
    }
    else
    {
        printf("%s is out of range.\n", s);
    }
    return(0);
}

int verify(int check)
{
    if(check < 0 || check > 100)
    {
        return FALSE;
    }
    return TRUE;
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
