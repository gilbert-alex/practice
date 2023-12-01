#include <stdio.h>
#include <ctype.h>

int main()
{
    char choice;

    puts("Meal Plans:");
    puts("A - Breakfast, Lunch, and Dinner");
    puts("B - Lunch and Dinner only");
    puts("C - Dinner only");
    printf("Your choice ");
    scanf("%c", &choice);

    choice = tolower(choice);

    printf("You've opted for ");

    switch(choice)
    {
    case 'a':
        printf("Breakfast, ");
    case 'b':
        printf("Lunch and ");
    case 'c':
        printf("Dinner ");
    default:
        printf("as your meal plan.\n");
    }
    return(0);
}
