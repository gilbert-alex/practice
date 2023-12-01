#include <stdio.h>

int main()
{
    char alpha;

    for(alpha='z'; alpha>='a'; alpha--)
    {
        printf("%c", alpha);
    }
    putchar('\n');
    return(0);
}
