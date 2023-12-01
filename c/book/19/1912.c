#include <stdio.h>

int main()
{
    char sample[] = "From whence cometh my help?\n";
    char *pc;
    pc = sample;

    while(*pc != '\0')
    {
        putchar(*pc);
        *pc++;
    }
    return(0);
}
