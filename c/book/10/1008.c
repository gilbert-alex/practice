#include <stdio.h>

void graph(int count, char character);

int main()
{
    int value = 2;

    while(value<=64)
    {
        graph(value,'=');
        printf("Value is %d\n",value);
        value=value*2;
    }
    return(0);
}

void graph(int count, char character)
{
    for(int x=0;x<count;x++)
    {
        putchar(character);
    }
    putchar('\n');
}
