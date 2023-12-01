#include <stdio.h>

int main()
{
    char first, second, third;

    for(first = 'A'; first <= 'Z'; first++)
    {
        for(second = 'A'; second <= 'Z'; second++)
        {
            for(third = 'A'; third <= 'Z'; third++)
            {
                printf("%c%c%c\n", first, second, third);
            }
        }
    }
    return 0;
}
