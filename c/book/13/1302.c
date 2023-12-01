#include <stdio.h>
#include <ctype.h>

int main()
{
    char phrase[] = "When in the Course of human events, it becomes.";

    int index, alpha, space, punct, upper, lower;

    alpha = space = punct = upper = lower = 0;

    index = 0;
    while (phrase[index])
    {
        if (isalpha(phrase[index]))
            alpha++;
        if (isspace(phrase[index]))
            space++;
        if (ispunct(phrase[index]))
            punct++;
        if (isupper(phrase[index]))
            upper++;
        if (islower(phrase[index]))
            lower++;
        index++;
    }

    printf("\"%s\"\n",phrase);
    puts("Statistics:");
    printf("%d alphabetic characters\n", alpha);
    printf("%d spaces\n", space);
    printf("%d punctuation symbols\n", punct);
    printf("%d upper case characters\n", upper);
    printf("%d lower case characters\n", lower);

    return(0);
}

