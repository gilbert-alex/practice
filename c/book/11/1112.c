#include <stdio.h>
#include <math.h>

int main()
{
    const float value = 2.0;

    int power;

    puts("The Holy Numbers of Computing.");
    for(power = 0; power <= 10; power++)
        printf("%.0f ^ %d = %.0f\n", value, power, pow(value,power));
    putchar('\n');

    return(0);
}

