#include <stdio.h>

int main()
{
    float x = -5.0;

    while(x<=5.0)
    {
        printf("%.1f\n", x);
        x += .5;
    }
    return 0;
}
