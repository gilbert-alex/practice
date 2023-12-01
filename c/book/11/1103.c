#include <stdio.h>

int main()
{
    int x;

    for(x=-5; x<5; x++)
    {
        printf("%d ", x);
    }
    for(x=x; x>=-5; x--)
    {
        printf("%d ", x);
    }
}
