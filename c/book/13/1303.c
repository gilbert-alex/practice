#include <stdio.h>
#include <ctype.h>

int main()
{
    char phrase[] = "When in the Course of human events, it becomes.";

    int index, alpha, space, punct, total;

    alpha = space = punct = total = 0;

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
        total++;
    }

    printf("\"%s\"\n",phrase);
    puts("Statistics:");
    printf("%d alphabetic characters\n", alpha);
    printf("%d spaces\n", space);
    printf("%d punctuation symbols\n", punct);
    printf("%d total characters\n", total);

    return(0);
}

