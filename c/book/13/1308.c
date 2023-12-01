#include <stdio.h>
#include <string.h>

int main()
{
    char password[] = "taco";
    char input[15];

    printf("Password: ");
    scanf("%s", input);

    if (!strcmp(input,password))
        puts("Password accepted.");
    else
        puts("Invalid password.");

    return(0);
}
