#include <stdio.h>
#include <stdlib.h>

int main()
{
    char *input;
    char *copy;
    int index;

    input = (char *)malloc(sizeof(char)*1024);
    copy = (char*)malloc(sizeof(char)*1024);
    if (input == NULL || copy == NULL)
    {
        puts("Unable to allocate memory");
        return(1);
    }

    puts("Type something long and boring ");
    fgets(input, 1024, stdin);

    index = 0;
    while(*(input + index) != '\n')
    {
        *(copy + index) = *(input + index);
        index++;
    }
    *(copy + index) = '\0';


    puts("You wrote: ");
    printf("\"%s\"\n", copy);
    return(1);
}
