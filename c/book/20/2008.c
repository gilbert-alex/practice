#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    char *input;
    int len;

    // allocate storage
    input = (char *)malloc(sizeof(char)*1024);
    if(input==NULL)
    {
        puts("Unable to allocate memory.");
        return(1);
    }

    // gather input
    puts("Type something long and boring.");
    fgets(input,1023,stdin);

    // resize the buffer
    len = strlen(input);
    input = realloc(input,sizeof(char)*len+1);
    if(input==NULL)
    {
        puts("Unable to reallocate buffer.");
        return(2);
    }
    puts("Memory reallocated.");

    // output results
    puts("You wrote:");
    printf("%s",input);

    return(0);
}
