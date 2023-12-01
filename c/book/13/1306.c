#include <stdio.h>
#include <ctype.h>

int main()
{
    char phrase[] = "ThiS Is a RANsom NoTE!";
    int index = 0;

    printf("Original: %s\n", phrase);
    printf("Modified: ");

    while (phrase[index])
    {
        if (isupper(phrase[index]))
            printf("%c", tolower(phrase[index]));
        else if (islower(phrase[index]))
            printf("%c", toupper(phrase[index]));
        else
            printf("%c", phrase[index]);
        index++;
    }
    return(0);
}
