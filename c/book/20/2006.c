#include <stdio.h>
#include <stdlib.h>

int main()
{
    unsigned char *junk;
    int x;

    junk = malloc(64);
    if (junk == NULL)
    {
        puts("Unable to allocate memory.");
        return(1);
    }

    for (x=0; x<64; x++)
    {
        printf("%02X ", *(junk+x));
        if( (x+1) % 8 == 0)
            putchar('\n');
    }
    return(0);
}
