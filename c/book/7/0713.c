#include <stdio.h>

int main()
{
    char firstname[15], lastname[15];

    printf("Type your first name: ");
    scanf("%s", firstname);
    printf("Type your last name: ");
    scanf("%s", lastname);
    printf("Hello, %s %s\n", firstname, lastname);
    return(0);
}
