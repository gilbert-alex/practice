#include <stdio.h>

int main()
{
    char firstname[15], lastname[15];

    printf("Type your first name: ");
    fgets(firstname, 15, stdin);
    printf("Type your last name: ");
    fgets(lastname, 15, stdin);
    printf("Hello, %s %s\n", firstname, lastname);
    return(0);
}
