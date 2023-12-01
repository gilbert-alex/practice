#include <stdio.h>

int main()
{
    char alpha = 'A';
    char *pa;

    pa = &alpha;

    for(int x = 0; x < 26; x++)
        putchar((*pa)++);
    printf("\n");

    printf("%c", *pa);
    return(0);
}
