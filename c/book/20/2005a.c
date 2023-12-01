#include <stdio.h>
#include <stdlib.h>

int main()
{
    const int bufsize = 1024;
    char *input, *output, *i, *o;

    input = (char *)malloc(sizeof(char)*bufsize);
    output = (char *)malloc(sizeof(char)*bufsize);
    if (input == NULL || output == NULL)
    {
        puts("Unable to allocate buffer.\n");
        return(1);
    }

    puts("Type something long and boring:");
    fgets(input,bufsize,stdin);

    i = input;
    o = output;
    while(*i != '\n')
    {
        *o = *i;
        o++;
        i++;
    }
    *o = '\0';

    puts("You wrote:");
    printf("\"%s\"\n",output);
    printf("i is:%c\n", *i);
    printf("o is:%c\n", *o);

    return(0);
}
