#include <stdio.h>

int main()
{
    float fav;

    printf("What is your favorite number: ");
    scanf("%f", &fav);
    printf("%0.1f is my favorite number, too!\n", fav);
    return(0);
}
