#include <stdio.h>
#include <stdlib.h>

int main()
{
    char *input;

    input = (char *)malloc(sizeof(char)*1024);
    if (input == NULL)
    {
        puts("Unable to allocate memory");
        return(1);
    }

    puts("Type something long and boring ");
    fgets(input, 1024, stdin);
    puts("You wrote:");
    printf("\"%s\"\n", input);

    return(0);
}
