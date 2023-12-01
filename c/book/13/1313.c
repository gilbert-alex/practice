#include <stdio.h>
#include <ctype.h>

int main()
{
    char phrase[] = "When in the Course of human events, it becomes.";

    int index, alpha, space, punct;

    alpha = space = punct = 0;

    index = 0;
    while (phrase[index])
    {
        if (isalpha(phrase[index]))
            alpha++;
        if (isspace(phrase[index]))
            space++;
        if (ispunct(phrase[index]))
            punct++;
        index++;
    }

    printf("\"%s\"\n",phrase);
    puts("Statistics:");
    printf("%5d alphabetic characters\n", alpha);
    printf("%5d spaces\n", space);
    printf("%5d punctuation symbols\n", punct);

    return(0);
}

