#include <stdio.h>

int main()
{
    const char name[4];

    printf("Who are you? ");
    fgets(name,4,stdin);
    printf("Glad to meet you, %s.\n", name);
    return(0);
}
