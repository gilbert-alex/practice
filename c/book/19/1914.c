#include <stdio.h>

int main()
{
    char sample[] = "From whence cometh my help?\n";
    char *ps;
    ps = sample;

    while (putchar(*(ps++)))
        ;
    return(0);
}
