#include <stdio.h>

int main()
{
    char firstname[16];
    char lastname[16];

    printf("What is your first name? ");
    scanf("%s",firstname);
    printf("What is your last name? ");
    scanf("%s",lastname);

    printf("Please to meet you, %s %s.\n",firstname,lastname);
    return(0);
}
